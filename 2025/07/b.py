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
    zip_longest,
)

import aocd

# import networkx as nx
from parse import parse

LINES = []


def solve(data: str):
    global LINES
    LINES = data.splitlines()[1:]
    return timeline(data.splitlines()[0].index("S"), 0)


@cache
def timeline(pos, line):
    while line < len(LINES) - 1:
        l = LINES[line + 1]
        for i, c in enumerate(l):
            if c == "^":
                if i == pos:
                    left = timeline(pos - 1, line + 1)
                    right = timeline(pos + 1, line + 1)
                    return left + right
        line += 1
    return 1


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    aocd.submit(answer, part="b", day=7, year=2025)
