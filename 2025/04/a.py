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

from utils.grid import defaultgrid

import aocd
import networkx as nx
from parse import parse

MOORE = lambda dimension=2: [p for p in product((-1, 0, 1), repeat=dimension) if any(p)]


def neighbors(cell):
    return [tuple(map(sum, zip(cell, d))) for d in MOORE()]


def solve(data: str):
    grid = defaultgrid(data)
    movable = 0
    for cell in list(grid):
        if grid[cell] == "@":
            if len([n for n in neighbors(cell) if grid[n] == "@"]) < 4:
                movable += 1
    return movable


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    aocd.submit(answer, part="a", day=4, year=2025)
