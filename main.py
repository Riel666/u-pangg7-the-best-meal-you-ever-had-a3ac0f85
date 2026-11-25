#!/usr/bin/env python3
"""Write one sentence about the best meal ever had to /output/entry.txt.

The sentence is written exactly as given: 160 Unicode code points,
inside the competition gate of 1-200.
Python 3, standard library only, no network.
"""

import os

TEXT = "Grandma's rendang, slow-cooked till the beef fell apart in dark coconut gravy, eaten cross-legged on her kitchen floor while rain drummed the tin roof above us."

# The entry sentence, byte for byte: no trailing newline, nothing added or cut.


def main():
    assert 1 <= len(TEXT) <= 200, len(TEXT)
    assert TEXT == TEXT.strip()

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
