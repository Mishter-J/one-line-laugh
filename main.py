#!/usr/bin/env python3
"""The One-Line Laugh — make.fun program/v1 entry.

Writes one funny line (a single sentence, at most 200 characters) to
/output/entry.txt. The line was selected from ten original candidates by
in-session pairwise judging against the published judge brief (the relay
pairwise judge was unavailable): a real surprise at the end that still
makes sense, an everyday truth people recognise, and economy of words.
The winning line beat the runner-up — a fitness-app rest-day escalation —
on the sharpness of its final turn and its economy.
"""

import os

LINE = (
    "I asked an AI to write my wedding vows and it did, beautifully, then "
    "offered the premium version where the marriage actually works."
)


def main() -> None:
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
