#!/usr/bin/env python3
"""Two Lines to Your Past Self.

Writes a two-line warning to my past self about one specific moment
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Python 3.13 standard library only; deterministic, no network.
"""

import os

TEXT = (
    "When your brother calls at 2am, don't let it ring out on the kitchen table — pick it up.\n"
    "That five-minute call is the night he finally asks for help, and answering is the reason he is still alive to call again."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
