#! /usr/bin/env python3

from itertools import product

import aocd

DIRS = [p for p in product((-1, 0, 1), repeat=3) if sum(map(int, map(bool, p))) == 1]


def nbrs(pos):
    return [tuple(map(sum, zip(pos, d))) for d in DIRS]


def solve(data: str):
    cubes = set()
    for l in data.splitlines():
        cubes.add(tuple(map(int, l.split(","))))
    area = 6 * len(cubes)
    for c in cubes:
        for n in nbrs(c):
            if n in cubes:
                area -= 1
    return area


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    aocd.submit(answer, part="a", day=18, year=2022)
