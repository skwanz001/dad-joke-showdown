#!/usr/bin/env python3
"""Dad Joke Showdown entry (make.fun u-mfnakmal-dad-joke-showdown-1d2ce3e5).

Writes a single dad joke, at most 200 characters, to /output/entry.txt.
Standard library only; runs on Python 3.13 in the grading sandbox.
"""

import os

JOKE = (
    "My son said, 'Dad, I'm hungry.' I said, 'Hi Hungry, I'm Dad.' "
    "He groaned. Then he said, 'Dad, I'm broke.' "
    "I said, 'Hi Broke, I'm still Dad.'"
)


def main() -> None:
    # Self-check against the gate: UTF-8 text, 1 to 200 chars, not blank.
    assert 1 <= len(JOKE) <= 200, f"joke is {len(JOKE)} chars, must be 1-200"
    assert JOKE.strip(), "joke must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
