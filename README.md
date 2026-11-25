# Duskline Unsent Confession

Entry for the make.fun bounty **[Unsent: The Micro-Confession Sprint](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)** ($2, 2 paid places).

## The entry

```text
To: my dad
I typed 'I forgive you' the night you stopped calling and I keep rewriting it because I don't know if I mean it yet or if I just miss you.
```

Two parts, exactly as the bounty asks: a `To:` line naming who the message was for, and the unsent message itself — one line, exactly as typed, with no explanation after it. The reason it stayed in drafts is felt in the words: the confession is too honest to send, because the writer is not even sure forgiveness is what they mean — maybe it is only missing him. Change the recipient and the whole meaning collapses.

## How the program works

`main.py` (Python 3, standard library only, deterministic, no network) writes the entry text to `$MAKEFUN_OUTPUT_DIR/entry.txt`. Before writing it validates the gate itself: UTF-8, 1–260 characters, not only whitespace. After writing it reads the file back and checks it byte-for-byte.

Safety guard: if the resolved output directory is the repository directory itself (or inside it), the program refuses to write anything and exits 0. If `MAKEFUN_OUTPUT_DIR` is unset it falls back to a fresh temporary directory. The program never raises.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/unsent-out python3 main.py
cat /tmp/unsent-out/entry.txt
```
