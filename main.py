#!/usr/bin/env python3
"""One Line of Earned Pride — writes a single line of earned pride to /output/entry.txt.

The line: after four failed driving tests, sixty-two-year-old Mara parks the
truck dead straight between the lines and sits a minute longer, hands still
on the wheel. The pride is never named; the reader feels it in the last clause.
"""

import os
import sys

ENTRY = (
    "She'd failed her driving test four times; this morning, at sixty-two, "
    "Mara parked the truck dead straight between the lines, then sat a minute "
    "longer, hands still on the wheel."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> None:
    """Gate: /output/entry.txt must be UTF-8 text of 1 to 240 characters,
    not only white space. Fails loudly otherwise."""
    if not text or not text.strip():
        raise ValueError("gate failed: entry is blank or only white space")
    if len(text) > 240:
        raise ValueError(
            f"gate failed: entry is {len(text)} characters, over the 240 limit"
        )
    text.encode("utf-8")  # raises UnicodeEncodeError if not valid UTF-8 text


def main() -> None:
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Verify what was actually written, not just what we intended to write.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    validate(written)
    if written != ENTRY:
        raise ValueError("gate failed: written file differs from entry text")
    print(f"wrote {len(written)} characters to {OUTPUT_PATH}")
    print(f"gate OK: 1 <= {len(written)} <= 240, non-blank, UTF-8")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)
