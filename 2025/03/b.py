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
    total = 0
    for l in data.splitlines():
        digits = []
        start = 0
        for i in range(12):
            end = -(11 - i)
            digits.append(max(set(l[start : (end if end < 0 else len(l))])))
            start = l.index(digits[-1], start) + 1
        num = 0
        for i, d in enumerate(digits):
            num += int(d) * 10 ** (11 - i)
        total += num
    return total


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    aocd.submit(answer, part="a", day=3, year=2025)
