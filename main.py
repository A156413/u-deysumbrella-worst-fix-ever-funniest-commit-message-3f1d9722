#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message -- make.fun entry.

Writes a single commit message, one line, for the bug fix that made
everything worse, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Deterministic: no network, no randomness, no clock.
"""
import os

ENTRY_TEXT = "hotfix: the bug is now officially a feature — updated the docs to agree with me"
# Why this line: the fix didn't fix anything -- it surrendered and
# rewrote the documentation so the bug looks intentional. The joke is
# the specific irony of a repair that broke more than it mended, told
# in the flat voice of a tired engineer at the end of a bad day.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)
    os.chmod(path, 0o644)
    print(ENTRY_TEXT)


if __name__ == "__main__":
    main()
