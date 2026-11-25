"""Duskline Unsent Confession — make.fun entry generator.

Writes one micro-confession to $MAKEFUN_OUTPUT_DIR/entry.txt.

The entry is exactly two parts:
  1. a "To:" line naming who the message was for, and
  2. the unsent message itself, one line exactly as typed.

Deterministic, stdlib only, no network. Never raises: any failure
to write exits 0 without writing anything. Never writes into the
repository directory.
"""

import os
import sys
import tempfile

ENTRY_TEXT = (
    "To: my dad\n"
    "I typed 'I forgive you' the night you stopped calling and I keep "
    "rewriting it because I don't know if I mean it yet or if I just miss you."
)

REPO_DIR = os.path.dirname(os.path.abspath(__file__))


def _is_inside_repo(path):
    try:
        repo = os.path.realpath(REPO_DIR)
        target = os.path.realpath(path)
        return target == repo or target.startswith(repo + os.sep)
    except Exception:
        return True


def main():
    try:
        out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or ""
        if not out_dir:
            out_dir = tempfile.mkdtemp(prefix="duskline-unsent-")
        out_dir = os.path.realpath(out_dir)

        # HARD GUARD: never write into the repo (or the repo itself).
        if _is_inside_repo(out_dir):
            return 0

        # Gate validation before writing.
        text = ENTRY_TEXT
        if not (1 <= len(text) <= 260):
            return 0
        if not text.strip():
            return 0
        text.encode("utf-8")

        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)

        # Read back and verify.
        with open(path, "r", encoding="utf-8") as f:
            back = f.read()
        if back != text:
            return 0
        return 0
    except Exception:
        return 0


if __name__ == "__main__":
    sys.exit(main())
