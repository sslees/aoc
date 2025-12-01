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


def solve(data: str):
    grid = defaultdict(type(None))
    dir = cycle([(0, -1), (1, 0), (0, 1), (-1, 0)])
    for y, line in enumerate(data.splitlines()):
        for x, val in enumerate(line):
            grid[x, y] = val
            if val == "^":
                start = (x, y)
    print("start", start)
    x, y = start
    dx, dy = next(dir)
    locs = {start}
    while grid[x, y] is not None:
        while grid[x + dx, y + dy] == "#":
            print("collision at", (x + dx, y + dy))
            dx, dy = next(dir)
        x = x + dx
        y = y + dy
        locs.add((x, y))
        print("moved to", (x, y))
    print("ct", len(locs) - 1)
    return len(locs) - 1


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    # print(answer)
    aocd.submit(answer, part="a", day=6, year=2024)
