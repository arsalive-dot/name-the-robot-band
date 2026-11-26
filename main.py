#!/usr/bin/env python3
"""Name the Robot Band — make.fun entry.

Writes one funny robot band name plus a few words on its hit song
to /output/entry.txt, inside the 1-200 character gate, on a single line.
"""

import os

ENTRY = "Blue Screen of Death Metal \u2014 hit single \u2018Ctrl+Alt+Delete My Number\u2019"


def verify(text):
    """Gate self-check: 1-200 chars, single line, not only whitespace."""
    stripped = text.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, gate is 1-200"
    assert "\n" not in stripped, "entry must be a single line"
    assert stripped, "entry must not be only whitespace"
    return True


def main():
    verify(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    tmp_path = os.path.join(out_dir, ".entry.txt.tmp")
    final_path = os.path.join(out_dir, "entry.txt")
    with open(tmp_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    os.replace(tmp_path, final_path)
    os.chmod(final_path, 0o644)


if __name__ == "__main__":
    main()
