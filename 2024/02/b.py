#! /usr/bin/env python3

from itertools import pairwise


def safe(levels):
    ds = [b - a for a, b in pairwise(levels)]
    return all(d in range(1, 4) for d in ds) or all(d in range(-3, 0) for d in ds)


def solve(data: str):
    ct = 0
    for l in data.splitlines():
        levels = [int(s) for s in l.split()]
        for skip in range(-1, len(levels)):
            if safe([e for i, e in enumerate(levels) if i != skip]):
                ct += 1
                break
    return ct


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
