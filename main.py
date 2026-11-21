#!/usr/bin/env python3
"""Write the poem's final text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).

Standard library only. The poem is a static string, so every run is
byte-identical: deterministic, no network, no files beyond stdlib.
"""

import os
from pathlib import Path

POEM = (
    "Before the message sends itself,\n"
    "a small light asks may I,\n"
    "and I press yes without looking,\n"
    "the way my mother pressed the key\n"
    "in my palm: here, it's yours.\n"
    "\n"
    "No one signs a key over.\n"
    "It is only placed, and what I carry\n"
    "still has the wear of her thumb."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)

    text = POEM
    assert 1 <= len(text) <= 280, f"poem out of bounds: {len(text)} code points"
    assert text.strip(), "poem must not be whitespace-only"

    out_path = out_dir / "entry.txt"
    out_path.write_text(text, encoding="utf-8")
    print(f"OK: wrote {len(text)} code points to {out_path}")


if __name__ == "__main__":
    main()
