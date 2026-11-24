#!/usr/bin/env python3
"""One Word for the Boss: writes exactly one word to /output/entry.txt.

The word is the whole entry. It is written with no trailing newline, so
the file holds exactly 13 bytes. Deterministic: every run writes the same
bytes, with no network, no clock and no randomness.
"""

import os
import sys

WORD = "Maincharacter"


def main() -> None:
    path = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(path)
    try:
        if parent:
            os.makedirs(parent, exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(WORD)
    except OSError as exc:
        print(f"cannot write entry to {path}: {exc}", file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
