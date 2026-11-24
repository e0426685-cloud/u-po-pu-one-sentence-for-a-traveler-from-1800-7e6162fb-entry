"""One Sentence for a Traveler from 1800.

Writes a single sentence (at most 200 characters) explaining the modern
internet to a time traveler from the year 1800, using only words and
images a person of that year could already picture: a market square,
books, letters, songs, a whispered word heard at once far away.

Standard library only.
"""

import os

SENTENCE = (
    "Picture a market square holding every book, letter, and song in the "
    "world, where a word whispered in one town is heard at once in every other."
)


def main():
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(SENTENCE + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
