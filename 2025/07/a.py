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


def solve(data: str):
    beams = {data.splitlines()[0].index("S")}
    splits = 0
    for l in data.splitlines()[1:]:
        for i, c in enumerate(l):
            if c == "^":
                if i in beams:
                    beams.remove(i)
                    beams.add(i + 1)
                    beams.add(i - 1)
                    splits += 1
    return splits


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    aocd.submit(answer, part="a", day=7, year=2025)
