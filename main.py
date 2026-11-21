#!/usr/bin/env python3
"""Write the poem's final text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).

Standard library only. The poem is a static string, so every run is
byte-identical: deterministic, no network, no files beyond stdlib.
"""

import os
from pathlib import Path

POEM = (
    "It asks nothing out loud.\n"
    "Before coffee, forty asks,\n"
    "and forty yeses, the way a floor\n"
    "takes weight.\n"
    "\n"
    "The forty-first waits at my desk.\n"
    "I look up: a week of mornings,\n"
    "held by a thing that keeps the hours.\n"
    "\n"
    "I say the yes slowly,\n"
    "and it sits in my mouth\n"
    "a week."
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
