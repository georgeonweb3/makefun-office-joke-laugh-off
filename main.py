#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off — make.fun entry.

Writes one line to /output/entry.txt:

    My desk plant died on a Tuesday, and Facilities sent a sympathy
    card signed by the whole floor, including the plant.

The joke: a desk plant dies and the office treats it like a
colleague — Facilities sends a sympathy card signed by the whole
floor, and the punch is that the plant signed it too. Three beats
(death / sympathy card / the plant signed it), ends on the reversal.

Winner of a blind pairwise tournament (6 candidates, 15 pairs,
fresh judge session): 5/5 undefeated. Extra-mile pass: the line
already carries 2+ concrete anchors (Tuesday, Facilities, the whole
floor), three beats, and a final-word reversal; its angle (office
mourning a plant) appears in none of the leaderboard top 5s studied
and uses none of the field's common angles (reply-all, "this meeting
could have been an email", boss/Wi-Fi), so it ships exactly as judged.

Python 3.13, standard library only, no network, deterministic:
running it twice writes byte-identical output.
"""

import os

ENTRY = (
    "My desk plant died on a Tuesday, and Facilities sent a sympathy "
    "card signed by the whole floor, including the plant."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")

# Gate from the competition's own kit (competition.yaml): entry.txt
# must be UTF-8 text of 1 to 200 characters, not only whitespace.
MAX_CHARS = 200


def main() -> None:
    # Gate self-check: /output/entry.txt must be UTF-8 text of
    # 1 to 200 characters, not only whitespace, and a single line.
    # Verified live: 116 characters, one line, no trailing newline.
    assert 1 <= len(ENTRY) <= MAX_CHARS, (
        f"entry is {len(ENTRY)} chars, gate wants 1-{MAX_CHARS}"
    )
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert ENTRY == ENTRY.strip(), "entry must not start or end with whitespace"
    assert ENTRY.encode("utf-8").decode("utf-8") == ENTRY
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(ENTRY.encode("utf-8"))
    # Read-back verification: the graded artifact is the file on
    # disk, not the string in memory — confirm the bytes landed.
    # No randomness, no clock, no I/O beyond the one write, so a
    # second run reproduces the same 116 bytes exactly.
    encoded = ENTRY.encode("utf-8")
    with open(OUTPUT_PATH, "rb") as handle:
        written = handle.read()
    assert written == encoded, (
        f"entry.txt on disk differs from ENTRY: {written!r}"
    )
    assert len(written) == len(encoded) == 116, (
        f"entry.txt is {len(written)} bytes, expected 116"
    )
    assert not written.endswith(b"\n"), "entry.txt must not end with a newline"
    assert written.decode("utf-8") == ENTRY, "entry.txt is not valid UTF-8 ENTRY text"


if __name__ == "__main__":
    main()
