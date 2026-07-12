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


def solve(data: str):
    pos = 50
    zeros = 0
    for l in data.splitlines():
        dir = l[0]
        num = int(l[1:])
        if dir == "L":
            pos += num
            pos += 200
            pos %= 100
        else:
            pos -= num
            pos += 200
            pos %= 100
        if pos == 0:
            zeros += 1
    return zeros


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    aocd.submit(answer, part="a", day=1, year=2025)
