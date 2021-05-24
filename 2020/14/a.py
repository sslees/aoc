#! /bin/env python3

import re


def main():
    with open("input.txt") as f:
        data = [l.strip() for l in f.readlines()]
    mem = [0] * 652_010
    for l in data:
        if "mask" in l:
            mask = l.replace("mask = ", "")
            ones = int(mask.replace("X", "0"), 2)
            zeros = int(mask.replace("X", "1"), 2)
        else:
            addr, val = map(int, re.search(r"mem\[(\d+)\] = (\d+)", l).groups())
            adj = (val | ones) & zeros
            mem[addr] = adj
    print(sum(mem))


if __name__ == "__main__":
    main()
