#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest entry.

Writes a short, funny rant about an everyday annoyance
(a printer failing on deadline day) to /output/entry.txt.
"""

import os

ENTRY_TEXT = (
    "The printer has ONE job and it chose today, the deadline day, "
    "to develop a personality. It is not out of ink. "
    "It is out of respect."
)


def main() -> None:
    # The gate reads exactly this path; write UTF-8 with no extra newline
    # so the output is byte-identical on every run.
    output_path = "/output/entry.txt"
    output_dir = os.path.dirname(output_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
