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
    rngs, ids = data.split("\n\n")
    good = 0
    largest = 0
    for a, b in sorted([tuple(parse("{:d}-{:d}", l)) for l in rngs.splitlines()]):
        a = max(a, largest + 1)
        if a <= b:
            good += b - a + 1
            largest = b
    return good


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    aocd.submit(answer, part="b", day=5, year=2025)
