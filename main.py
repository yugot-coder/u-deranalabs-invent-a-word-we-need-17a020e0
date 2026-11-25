"""Invent a Word We Need.

The entry coins one new English word and defines it in a single clear
line: Chairdrobe — the chair that holds clothes too clean to wash and
too worn to put away. A blend of "chair" and "wardrobe": the piece of
furniture almost every bedroom already has, which no dictionary names.

Standard library only. Deterministic: no randomness, no network, no
clock. The entry is the line at ENTRY, written to
<MAKEFUN_OUTPUT_DIR>/entry.txt (default /output/entry.txt).
"""

import os

ENTRY = (
    "Chairdrobe (n.) the chair that holds clothes too clean to wash "
    "and too worn to put away."
)


def validate_entry(text):
    """Check the entry against the competition gate.

    The gate requires UTF-8 text of 1 to 140 characters, not only
    white space. Returns the entry unchanged when it passes, and
    raises AssertionError with a plain message when it does not.
    """
    assert text.strip(), "entry must not be empty or only white space"
    assert 1 <= len(text) <= 140, "entry must be 1 to 140 characters"
    text.encode("utf-8")
    lines = text.splitlines()
    assert len(lines) == 1, "entry must be a single line"
    return text


def main():
    """Validate the entry, write it to entry.txt, and read it back."""
    entry = validate_entry(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(entry + "\n")
    # Read-back validation: the file we just wrote must hold exactly
    # the entry we meant to write, nothing else.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == entry + "\n", "entry.txt does not match the entry"
    print(entry)


if __name__ == "__main__":
    main()
