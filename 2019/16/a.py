#! /usr/bin/env python3

from itertools import chain, cycle, repeat
from operator import mul


def pattern(i):
    pat = cycle(chain(*(repeat(e, i + 1) for e in [0, 1, 0, -1])))
    next(pat)
    return pat


def solve(data: str):
    data = [int(c) for c in data]
    for _ in range(100):
        data = [abs(sum(map(mul, data, pattern(i)))) % 10 for i in range(len(data))]
    return "".join(map(str, data[:8]))


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
