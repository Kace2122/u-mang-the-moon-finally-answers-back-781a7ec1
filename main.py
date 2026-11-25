#!/usr/bin/env python3
"""The Moon Finally Answers Back — u-mang-the-moon-finally-answers-back-781a7ec1.

Writes one line, the Moon's comeback, to /output/entry.txt.
Deterministic: the same line, byte for byte, on every run.
"""

import os

ENTRY = (
    "Four billion years of wishes, howls and 3 a.m. promises, "
    "and not one of you has ever asked how I'm doing \u2014 "
    "I'm fine, by the way. Tired, but fine."
)


def main() -> None:
    # Gate self-check: one line, 1-240 chars, not only whitespace.
    text = ENTRY.strip()
    assert 1 <= len(ENTRY) <= 240, f"entry {len(ENTRY)} chars, must be 1-240"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert text, "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
