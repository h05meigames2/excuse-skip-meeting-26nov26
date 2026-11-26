#!/usr/bin/env python3
"""The Funniest Excuse for Skipping a Meeting - make.fun bounty entry.

Writes a single original one-line excuse (at most 200 characters) to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
Stdlib only, no network.
"""

import os

EXCUSE = (
    "I didn't skip the meeting \u2014 my calendar read the invite, saw no agenda, "
    "and declined on my behalf. It has boundaries I can only dream of."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    excuse = EXCUSE.strip()
    assert 1 <= len(excuse) <= 200, f"entry is {len(excuse)} chars, must be 1-200"
    assert "\n" not in excuse, "entry must be a single line"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(excuse + "\n")
    print(f"Wrote {len(excuse)}-char entry to {path}: {excuse}")


if __name__ == "__main__":
    main()
