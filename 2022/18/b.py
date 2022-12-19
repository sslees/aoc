#! /usr/bin/env python3

from functools import cache
from itertools import product

import aocd

DIRS = [p for p in product((-1, 0, 1), repeat=3) if sum(map(int, map(bool, p))) == 1]


@cache
def valid(p):
    x, y, z = p
    return -1 <= x <= 20 and -1 <= y <= 20 and -1 <= z <= 20


@cache
def nbrs(pos):
    return [p for d in DIRS if valid(p := tuple(map(sum, zip(pos, d))))]


def solve(data: str):
    rock = set()
    for l in data.splitlines():
        rock.add(tuple(map(int, l.split(","))))
    water = {(-1, -1, -1)}
    seen = set()
    while len(water) > len(seen):
        for p in list(water):
            if p not in seen:
                seen.add(p)
                for n in nbrs(p):
                    if valid(n) and n not in rock:
                        water.add(n)
    area = 6 * len(water)
    for c in water:
        for n in nbrs(c):
            if n in water:
                area -= 1
    return area - 22**2 * 6


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    aocd.submit(answer, part="b", day=18, year=2022)
