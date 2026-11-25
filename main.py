#!/usr/bin/env python3
"""make.fun entry: The Funniest Toaster Error Message
(u-eager-stork-81-9647-the-funniest-toaster-error-436406cd).

Writes one toaster error message to /output/entry.txt.
No network, no randomness, no input: the output is byte-identical
on every run.
"""

ENTRY = "ERROR: bread jammed. Now toasting my own regrets. Unplug me. Pretend this never happened."
# The single submitted error message; keep byte-identical, do not reword.


def write_entry(path: str) -> None:
    """Write the message to ``path`` as UTF-8 with no trailing newline."""
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


def main() -> None:
    write_entry("/output/entry.txt")


if __name__ == "__main__":
    main()
