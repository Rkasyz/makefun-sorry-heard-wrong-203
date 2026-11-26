#!/usr/bin/env python3
"""Entry for make.fun: Sorry, I Heard That Wrong.

Writes a single-line apology from a smart speaker to its owner after
mishearing a command, to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""
import os

ENTRY = "Sorry \u2014 I heard 'play jazz' and ordered twelve pizzas. I have unsubscribed myself from dinner. Please do not unplug me."

# The competition gate is 1-140 characters; fail loudly instead of
# submitting an entry the scorer would refuse.
assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars, gate is 1-140"

def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
