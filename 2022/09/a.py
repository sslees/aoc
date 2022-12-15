#! /usr/bin/env python3

from itertools import product

import aocd
from parse import parse

MOVES = {
    "U": (0, -1),
    "D": (0, 1),
    "L": (-1, 0),
    "R": (1, 0),
}
DIRS = [(dx, dy) for dx, dy in product((-1, 0, 1), repeat=2) if dx or dy]


def nbrs(pos):
    return [tuple(map(sum, zip(pos, d))) for d in DIRS]


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def dist(a, b):
    return max(abs(b[0] - a[0]), abs(b[1] - a[1]))


def manhattan(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])


def solve(data: str):
    head = (0, 0)
    tail = (0, 0)
    locs = {(0, 0)}
    for l in data.splitlines():
        d, n = parse("{} {:d}", l)
        for _ in range(n):
            head = add(head, MOVES[d])
            if dist(head, tail) > 1:
                tail = min(nbrs(tail), key=lambda nbr: manhattan(head, nbr))
                locs.add(tail)
    return len(locs)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    aocd.submit(answer, part="a", day=9, year=2022)
