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

WIDTH = 101
HEIGHT = 103
# WIDTH = 11
# HEIGHT = 7
TIME = 100

from operator import mul


def solve(data: str):
    quads = Counter()
    for l in data.splitlines():
        px, py, vx, vy = parse("p={:d},{:d} v={:d},{:d}", l)
        x = (px + TIME * vx) % WIDTH
        y = (py + TIME * vy) % HEIGHT
        print("final", x, y)
        if x < WIDTH // 2 and y < HEIGHT // 2:
            quads[0] += 1
        elif x > WIDTH // 2 and y < HEIGHT // 2:
            quads[1] += 1
        elif x < WIDTH // 2 and y > HEIGHT // 2:
            quads[2] += 1
        elif x > WIDTH // 2 and y > HEIGHT // 2:
            quads[3] += 1
    print(list(quads.values()))
    return math.prod(quads.values())


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    # print(answer)
    aocd.submit(answer, part="a", day=14, year=2024)
