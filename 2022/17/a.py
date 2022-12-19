#! /usr/bin/env python3

import math
import random
import re
import statistics
from collections import Counter, defaultdict, deque, namedtuple
from functools import cache
from itertools import combinations, count, cycle, permutations, product, repeat

import aocd
import networkx as nx
from parse import parse

SHAPES = [
    ((0, 0), (1, 0), (2, 0), (3, 0)),
    ((0, 1), (1, 0), (1, 1), (1, 2), (2, 1)),
    ((0, 0), (1, 0), (2, 0), (2, 1), (2, 2)),
    ((0, 0), (0, 1), (0, 2), (0, 3)),
    ((0, 0), (0, 1), (1, 0), (1, 1)),
]
LEFT = -1, 0
RIGHT = 1, 0
DOWN = 0, -1


def pretty(shape, rocks, ymax):
    for y in range(ymax + 7, -1, -1):
        print(
            "".join(
                "#" if (x, y) in rocks else "@" if (x, y) in shape else "."
                for x in range(7)
            )
        )
    print()


def move(shape, dx, dy):
    # if (dx, dy) == LEFT:
    #     # print(f"first point at {shape[0]}, moving LEFT")
    # if (dx, dy) == RIGHT:
    #     # print(f"first point at {shape[0]}, moving RIGHT")
    # if (dx, dy) == DOWN:
    #     # print(f"first point at {shape[0]}, moving DOWN")
    return tuple((x + dx, y + dy) for x, y in shape)


def valid(shape, rocks):
    invalid = any(y < 0 or x < 0 or x > 6 or (x, y) in rocks for x, y in shape)
    # if invalid:
    #     for x, y in shape:
    #         if y < 0:
    # print("INVALID move (y too DOWN)")
    #         if x < 0:
    # print("INVALID move (x too LEFT)")
    #         if x > 6:
    # print("INVALID move (x too RIGHT)")
    #         if (x, y) in rocks:
    # print("INVALID move (collision w/ rock)")
    return not invalid


def solve(data: str):
    shapes = cycle(SHAPES)
    dirs = cycle([c for c in data])
    rocks = set()
    ymax = -1
    for _ in range(2_022):
        # for _ in range(11):
        shape = next(shapes)
        # print(f"new shape INDEX {SHAPES.index(shape)} w/ delta (2, {ymax + 4})")
        shape = move(shape, 2, ymax + 4)
        # pretty(shape, rocks, ymax)
        while True:
            shape2 = move(shape, *(LEFT if next(dirs) == "<" else RIGHT))
            shape = shape2 if valid(shape2, rocks) else shape
            shape2 = move(shape, *DOWN)
            if not valid(shape2, rocks):
                # print(f"rock resting with point at ({shape[0]})")
                for p in shape:
                    rocks.add(p)
                ymax = max(ymax, max(y for _, y in shape))
                break
            else:
                shape = shape2
    return ymax + 1


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    aocd.submit(answer, part="a", day=17, year=2022)
