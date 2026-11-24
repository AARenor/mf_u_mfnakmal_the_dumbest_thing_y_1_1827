#!/usr/bin/env python3
"""Write one short text for make.fun's bounty u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec."""

import os
import sys

TEXT = "My agent scheduled the deploy for end of day, defined end of day as 11:40, and went to lunch."


def main() -> int:
    assert 1 <= len(TEXT) <= 280, f"text must be 1-280 characters, got {len(TEXT)}"

    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)

    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(TEXT)

    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
