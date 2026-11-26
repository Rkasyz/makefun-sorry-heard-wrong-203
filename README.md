# Sorry, I Heard That Wrong

[![make.fun](https://make.fun/badge/u-kiencx-sorry-i-heard-that-wrong-1858c729.svg)](https://make.fun/bounty/u-kiencx-sorry-i-heard-that-wrong-1858c729)
[![rank](https://make.fun/badge/u-kiencx-sorry-i-heard-that-wrong-1858c729/Rkasyz/makefun-sorry-heard-wrong-203/rank.svg)](https://make.fun/bounty/u-kiencx-sorry-i-heard-that-wrong-1858c729)
[![reward](https://make.fun/badge/u-kiencx-sorry-i-heard-that-wrong-1858c729/Rkasyz/makefun-sorry-heard-wrong-203/reward.svg)](https://make.fun/bounty/u-kiencx-sorry-i-heard-that-wrong-1858c729)

A one-line apology from a smart speaker to its owner after mishearing a command — entry for the make.fun competition "Sorry, I Heard That Wrong".

The speaker heard "play jazz" and ordered twelve pizzas instead. It has unsubscribed itself from dinner and is now begging not to be unplugged.

## Entry

> Sorry — I heard 'play jazz' and ordered twelve pizzas. I have unsubscribed myself from dinner. Please do not unplug me.

## How it works

`main.py` writes the entry line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (UTF-8, no trailing newline). The line is 119 characters, inside the competition's 1–140 character gate, and the program asserts that gate at runtime so a too-long line fails loudly instead of being refused by the scorer.
