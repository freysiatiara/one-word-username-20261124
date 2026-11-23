"""One Word, One Username, One Reward — entry for freysiatiara.

The program writes exactly one word, our own make.fun username
"freysiatiara", to /output/entry.txt and nothing else. No newline,
no spaces, no explanation: twelve bytes, so the gate (UTF-8 text,
1 to 30 characters, not whitespace-only) passes and the judge reads
the handle itself — a genuine make.fun username, criterion 1 of the
judge's brief, sent as one word.
"""

import os
import sys

# The single word this entry sends: our own make.fun handle.
USERNAME = "freysiatiara"

# Where the harness reads the entry from. Overridable with
# ENTRY_OUTPUT only for local verification; the graded run
# always uses the default /output/entry.txt.
DEFAULT_OUTPUT = "/output/entry.txt"
OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", DEFAULT_OUTPUT)


def validate(path=OUTPUT_PATH, username=USERNAME):
    """Read the written file back and prove it holds exactly one
    word: the expected username, 1 to 30 UTF-8 characters, a single
    word with no spaces, and not whitespace-only. Returns True only
    when every check holds.
    """
    with open(path, "r", encoding="utf-8") as handle:
        content = handle.read()
    if content != username:
        return False
    if not 1 <= len(content) <= 30:
        return False
    if content != content.strip():
        return False
    if " " in content or content.isspace():
        return False
    return True


def write_username(path=OUTPUT_PATH, username=USERNAME):
    """Write exactly the username to path, no trailing newline."""
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(username)
    return path


if __name__ == "__main__":
    write_username()
    if not validate():
        print("validation failed: /output/entry.txt is not exactly "
              "'freysiatiara'", file=sys.stderr)
        sys.exit(1)
    sys.exit(0)
