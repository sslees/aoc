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

TOTAL = 1_000_000_000_000
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


def move(shape, dx, dy):
    return tuple((x + dx, y + dy) for x, y in shape)


def valid(shape, rocks):
    return not any(y < 0 or x < 0 or x > 6 or (x, y) in rocks for x, y in shape)


def solve(data: str):
    shapes = cycle(SHAPES)
    dirs = cycle([c for c in data])
    rocks = set()
    ymax = -1
    hist = []
    diffs = []
    diffs2 = []
    # _scale = 7
    _scale = 1
    di = math.lcm(len(SHAPES), len(data)) * _scale
    off = TOTAL % di
    for i in range(TOTAL):
        if i > di and i % di == off:
            # if len(hist) > 3:
            #     print(
            #         i,
            #         ymax,
            #         di,
            #         ":",
            #         ymax - hist[-1],
            #         hist[-1] - hist[-2],
            #         hist[-2] - hist[-3],
            #         hist[-3] - hist[-4],
            #     )
            #     assert (TOTAL - i) % di == 0
            #     return ymax + (TOTAL - i) // di * (ymax - hist[-1]) + 1
            if diffs2:
                print(ymax - hist[-1] - diffs[-1] - diffs2[-1])
            if diffs:
                diffs2.append(ymax - hist[-1] - diffs[-1])
            if hist:
                diffs.append(ymax - hist[-1])
            hist.append(ymax)
            assert (TOTAL - i) % di == 0
        shape = next(shapes)
        shape = move(shape, 2, ymax + 4)
        while True:
            shape2 = move(shape, *(LEFT if next(dirs) == "<" else RIGHT))
            shape = shape2 if valid(shape2, rocks) else shape
            shape2 = move(shape, *DOWN)
            if not valid(shape2, rocks):
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
    # aocd.submit(answer, part="b", day=17, year=2022)

"""
notes:
- the lcm finds when the towers will be identical
since the pieces and moves will line up again
- it's not stable for some reason, so use y''(x)
- also shuld see if input file has loops
- might need to use a different number than 7 for real
"""
