"""The Agent's Uh-Oh entry.

Writes exactly one word to /output/entry.txt: the word an agent says
when it has no idea what to do.

Deterministic: no clock, no randomness, no network, no model calls.
The word is 13 characters, inside the 1-99 gate.
"""

from pathlib import Path

# The entry word: a GPS that has lost the route, said out loud.
# One word, 13 characters, no punctuation, no explanation attached.
WORD = "recalculating"


def build_word() -> str:
    """Return the entry word.

    "recalculating" is the voice of a machine that has lost the route:
    a GPS blurting it out mid-journey when it no longer knows which
    way to turn. It is a genuine one-word reaction to being completely
    lost, it sounds like something an agent would actually say, it
    lands at a glance, and it is fresher than the first words anyone
    types for this prompt (uh-oh, oops, hmm). No caption needed: the
    joke is the word itself, in the voice of a machine stalling.
    """
    return WORD


def main() -> None:
    """Write the word to /output/entry.txt, exactly as the gate reads it.

    No trailing newline: the file holds the word alone, 13 characters
    of UTF-8, so the sealed scorer counts the word itself and nothing
    else.
    """
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(build_word(), encoding="utf-8")


if __name__ == "__main__":
    main()
