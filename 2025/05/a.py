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

# import networkx as nx
from parse import parse


def solve(data: str):
    ranges, ids = data.split("\n\n")
    check = []
    for l in ranges.splitlines():
        a, b = parse("{:d}-{:d}", l)
        check.append(range(a, b + 1))
    return len([i for i in ids.splitlines() if any(int(i) in r for r in check)])


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    aocd.submit(answer, part="a", day=5, year=2025)
