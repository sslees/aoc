#! /usr/bin/env python3

import math
import random
import re
import statistics
from collections import Counter, defaultdict, deque, namedtuple
from functools import cache
from itertools import (
    combinations,
    count,
    cycle,
    pairwise,
    permutations,
    product,
    repeat,
)

import aocd
import networkx as nx
from parse import parse
from utils.grid import defaultgrid
from utils.cells import VNEUMANN


def neighbors(p):
    return [tuple(map(sum, zip(p, d))) for d in VNEUMANN]


def solve(data: str):
    grid = defaultgrid(data)
    # width, height = dimensions(data)
    heads = [p for p, h in grid.items() if h != "." and int(h) == 0]
    print(heads)
    total = 0
    for head in heads:
        peaks = set()
        pts = deque([(head, 0)])
        while pts:
            p, h = pts.pop()
            for n in neighbors(p):
                if grid[n] not in (None, ".") and int(grid[n]) == h + 1:
                    if h + 1 == 9:
                        peaks.add(n)
                    else:
                        pts.appendleft((n, h + 1))
        total += len(peaks)
        print(len(peaks))
    return total


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    # print(answer)
    aocd.submit(answer, part="a", day=10, year=2024)
