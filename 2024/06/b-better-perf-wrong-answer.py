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


def attempt(grid, start):
    dirs = cycle("NESW")
    deltas = {"N": (0, -1), "E": (1, 0), "S": (0, 1), "W": (-1, 0)}
    # print("start", start)
    x, y = start
    dx, dy = deltas[next(dirs)]
    locs = {("N", start)}
    dir = None
    while grid[x, y] is not None:
        while grid[x + dx, y + dy] == "#":
            # print("collision at", (x + dx, y + dy))
            dir = next(dirs)
            dx, dy = deltas[dir]
        x = x + dx
        y = y + dy
        if (dir, (x, y)) in locs:
            # print("already here")
            return True
        locs.add((dir, (x, y)))
        # print("moved to", (x, y))
    # print("no loop")
    return [p for _, p in locs]


def solve(data: str):
    grid = defaultdict(type(None))
    for y, line in enumerate(data.splitlines()):
        for x, val in enumerate(line):
            grid[x, y] = val
            if val == "^":
                start = (x, y)
    locs = attempt(grid, start)
    ct = 0
    for x, y in locs:
        if grid[(x, y)] is not None and (x, y) != start:
            newgrid = grid.copy()
            newgrid[(x, y)] = "#"
            if attempt(newgrid, start) is True:
                ct += 1
    return ct


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    # aocd.submit(answer, part="b", day=6, year=2024)
