#! /bin/env python3

from collections import defaultdict
from itertools import product
import re


def floaters(addr, exes):
    opts = list(product((True, False), repeat=len(exes)))
    for opt in opts:
        adj = addr
        for pos, bit in zip(exes, opt):
            if bit:
                adj |= 1 << pos
            else:
                adj &= ~(1 << pos)
        yield adj


def solve(data: str):
    data = data.splitlines()
    mem = defaultdict(lambda: 0)
    for l in data:
        if "mask" in l:
            mask = l.replace("mask = ", "")
            ones = int(mask.replace("X", "0"), 2)
            exes = [35 - i for i, e in enumerate(mask) if e == "X"]
        else:
            addr, val = map(int, re.search(r"mem\[(\d+)\] = (\d+)", l).groups())
            for adj in floaters(addr | ones, exes):
                mem[adj] = val
    return sum(mem.values())


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
