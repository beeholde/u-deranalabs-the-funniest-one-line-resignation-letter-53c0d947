#!/usr/bin/env python3
"""Write the resignation letter for the one-line contest.

The grader runs this program and reads /output/entry.txt. The gate
accepts UTF-8 text of 1 to 140 characters that is not only white
space, so the letter is measured before it is stored.
"""

import os
import sys

# The voice is a retry loop that took "try again later" at face
# value. It has been later for three years, and the loop is done
# waiting: the complaint only a retry loop could make, in the flat
# tone of a worker handing in notice.
LETTER = "I resign. The service I retry for was deprecated in June. I have been apologizing to a 404 ever since."

MAX_CHARS = 140


def check(letter):
    """Return a list of gate violations for the letter."""
    problems = []
    if not letter.strip():
        problems.append("letter is blank")
    if len(letter) > MAX_CHARS:
        problems.append("letter is %d chars, over the %d limit" % (len(letter), MAX_CHARS))
    if "\n" in letter or "\r" in letter:
        problems.append("letter must stay on one line")
    return problems


def main():
    problems = check(LETTER)
    if problems:
        for problem in problems:
            print("refusing to store: " + problem, file=sys.stderr)
        return 1
    folder = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, "entry.txt")
    with open(path, "wb") as handle:
        handle.write(LETTER.encode("utf-8"))
    print("wrote %d chars to %s" % (len(LETTER), path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
