#! /usr/bin/env python3

from itertools import pairwise


def safe(levels):
    ds = [b - a for a, b in pairwise(levels)]
    return all(d in range(1, 4) for d in ds) or all(d in range(-3, 0) for d in ds)


def solve(data: str):
    return sum(1 for l in data.splitlines() if safe([int(s) for s in l.split()]))


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
