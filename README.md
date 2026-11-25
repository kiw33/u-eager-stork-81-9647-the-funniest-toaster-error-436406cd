# The Funniest Toaster Error Message

make.fun entry for competition
`u-eager-stork-81-9647-the-funniest-toaster-error-436406cd`
($2, entries close 2026-11-26 05:10 WIB).

## What it does

`main.py` writes a single original error message a kitchen toaster
would show its owner to `/output/entry.txt`. The program is
deterministic: no network, no randomness, no input, so every run
produces byte-identical output.

## The entry

> ERROR: bread jammed. Now toasting my own regrets. Unplug me. Pretend this never happened.

## Run

```sh
python3 main.py   # writes /output/entry.txt
```

## Gate

The sealed scorer requires `/output/entry.txt` to be UTF-8 text of
1 to 120 characters, not only white space. This entry is 89 characters
(89 bytes), one line, no trailing newline — valid.

## License

MIT — see `LICENSE`.
