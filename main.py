"""One Sentence for a Traveler from 1800.

Writes a single sentence (at most 200 characters) explaining the modern
internet to a time traveler from the year 1800, using only words and
images a person of that year could already picture: a market square,
books, letters, songs, a whispered word heard at once far away.

The program validates the sentence before writing it, writes it to
/output/entry.txt, and then reads the file back to confirm the written
content matches exactly. Standard library only.

Usage:
    python3 main.py
"""

import os

MAX_LENGTH = 200
OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")

SENTENCE = (
    "Picture a market square holding every book, letter, and song in the "
    "world, where a word whispered in one town is heard at once in every other."
)


def validate_sentence(text):
    """Check that the text is exactly one sentence within the limit.

    Returns a list of problems; an empty list means the text is valid.
    A sentence is counted by its terminal punctuation: one period,
    exclamation mark, or question mark at the end and none earlier.
    """
    problems = []
    stripped = text.strip()
    if not stripped:
        problems.append("sentence is empty")
    if len(stripped) > MAX_LENGTH:
        problems.append(
            "sentence is %d characters, over the %d limit"
            % (len(stripped), MAX_LENGTH)
        )
    terminators = sum(stripped.count(mark) for mark in ".!?")
    if terminators != 1:
        problems.append("expected exactly one sentence, found %d" % terminators)
    if stripped and stripped[-1] not in ".!?":
        problems.append("sentence does not end with terminal punctuation")
    return problems


def write_and_verify(path, text):
    """Write text to path, then read it back and confirm it matches.

    The file is created with plain open() and chmod 644 so any reader
    (not just the owner) can open it. Raises ValueError if the bytes
    read back differ from what was written.
    """
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    os.chmod(path, 0o644)
    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != text:
        raise ValueError("verification failed: file content does not match")


def main():
    problems = validate_sentence(SENTENCE)
    if problems:
        raise ValueError("invalid entry sentence: " + "; ".join(problems))
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    write_and_verify(OUTPUT_PATH, SENTENCE + "\n")
    print("wrote %d characters to %s" % (len(SENTENCE), OUTPUT_PATH))


if __name__ == "__main__":
    main()
