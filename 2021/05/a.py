#! /usr/bin/env python3

from collections import Counter

import aocd
from parse import parse


def points(x1, y1, x2, y2):
    if x1 == x2:
        if y1 < y2:
            return [(x1, y) for y in range(y1, y2 + 1)]
        return [(x1, y) for y in range(y1, y2 - 1, -1)]
    if y1 == y2:
        if x1 < x2:
            return [(x, y1) for x in range(x1, x2 + 1)]
        return [(x, y1) for x in range(x1, x2 - 1, -1)]


def solve(data: str):
    pts = Counter()
    for l in data.splitlines():
        x1, y1, x2, y2 = parse("{:d},{:d} -> {:d},{:d}", l)
        if x1 == x2 or y1 == y2:
            for p in points(x1, y1, x2, y2):
                pts[p] += 1
    return len([p for p in pts if pts[p] >= 2])


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    aocd.submit(answer, part="a", day=5, year=2021)
