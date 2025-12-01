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
from operator import mul

WIDTH = 101
HEIGHT = 103
TIME = 100


class Bot:
    def __init__(self, px, py, vx, vy):
        self.px = px
        self.py = py
        self.vx = vx
        self.vy = vy

    def step(self, grid):
        if grid[self.px, self.py] != 0:
            grid[self.px, self.py] -= 1
        self.px = (self.px + self.vx) % WIDTH
        self.py = (self.py + self.vy) % HEIGHT
        grid[self.px, self.py] += 1


def pretty(grid):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            n = grid[x, y]
            print("." if n == 0 else str(n) if n < 10 else "+", end="")
        print()
    print()


def symmetry(bots, grid):
    sym = 0
    for b in bots:
        if grid[WIDTH - b.px - 1, HEIGHT - b.py - 1] > 0:
            sym += 1
    return sym / len(bots)


def solve(data: str):
    bots: list[Bot] = []
    grid = Counter()
    for l in data.splitlines():
        bots.append(Bot(*parse("p={:d},{:d} v={:d},{:d}", l)))
    for t in count(1):
        for b in bots:
            b.step(grid)
        sym = symmetry(bots, grid)
        # print(sym)
        if sym > 0.1:
            print(t)
            pretty(grid)
            print()
    return


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    # aocd.submit(answer, part="b", day=14, year=2024)
