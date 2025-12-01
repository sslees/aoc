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
from utils.grid import defaultgrid, dimensions

DIRS = {"N": (0, -1), "E": (1, 0), "S": (0, 1), "W": (-1, 0)}


def add(p, d):
    return p[0] + d[0], p[1] + d[1]


# @profile
def best(grid, pos, dir, end, depth):
    # if depth > 600:
    #     raise
    if pos == end:
        return 0
    scores = []
    for d in DIRS:
        target = add(pos, DIRS[d])
        if grid[target] != "#":
            old = grid[pos]
            grid[pos] = "#"
            b = best(grid, target, d, end, depth + 1)
            if b is not None:
                if d == dir:
                    scores.append(1 + b)
                else:
                    scores.append(1001 + b)
            grid[pos] = old
    return min(scores) if scores else None


"""
make a graph of all the squares in the maze
but for each intersection, connect each perpendicular
pair of exits with a weight of 1002
then solve for the shortest path
"""


def solve(data: str):
    grid = defaultgrid(data)
    start = next(p for p, c in grid.items() if c == "S")
    end = next(p for p, c in grid.items() if c == "E")
    pos = start
    dir = "E"
    return best(grid, pos, dir, end, 0)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    # aocd.submit(answer, part="a", day=16, year=2024)
