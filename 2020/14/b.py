#! /bin/env python3

import collections
import itertools
import re


def floaters(addr, exes):
    opts = list(itertools.product((True, False), repeat=len(exes)))
    for opt in opts:
        adj = addr
        for pos, bit in zip(exes, opt):
            if bit:
                adj |= 1 << pos
            else:
                adj &= ~(1 << pos)
        yield adj


def main():
    with open("input.txt") as f:
        data = [l.strip() for l in f.readlines()]
    mem = collections.defaultdict(lambda: 0)
    for l in data:
        if "mask" in l:
            mask = l.replace("mask = ", "")
            ones = int(mask.replace("X", "0"), 2)
            exes = [35 - i for i, e in enumerate(mask) if e == "X"]
        else:
            addr, val = map(int, re.search(r"mem\[(\d+)\] = (\d+)", l).groups())
            for adj in floaters(addr | ones, exes):
                mem[adj] = val
    print(sum(mem.values()))


if __name__ == "__main__":
    main()
