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
    res = 0
    for l in data.splitlines():
        tens = max(set(l[:-1]))
        ones = max(set(l[l.index(tens) + 1 :]))
        res += int(tens) * 10 + int(ones)
    return res


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    aocd.submit(answer, part="a", day=3, year=2025)
