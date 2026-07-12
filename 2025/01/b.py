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
        print(pos, l)
        dir = l[0]
        num = int(l[1:])
        if dir == "R":
            for _ in range(num):
                pos += 1
                if pos == 100:
                    pos = 0
                if pos == 0:
                    zeros += 1
        else:
            for _ in range(num):
                pos -= 1
                if pos == -1:
                    pos = 99
                if pos == 0:
                    zeros += 1
    return zeros


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    aocd.submit(answer, part="b", day=1, year=2025)
