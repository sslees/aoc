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
    # for i in [int(c) for c in data]:
    # for i in [int(s) for s in data.split(",")]:
    # for i in [int(l) for l in data.splitlines()]:
    # for c in data:
    invalids = 0
    for r in data.replace("\n", "").split(","):
        # print("testing range", r)
        a, b = r.split("-")
        for i in range(int(a), int(b) + 1):
            id = str(i)
            # print("testing id", id)
            if id[: len(id) // 2] == id[len(id) // 2 :]:
                # print("invalid", id)
                invalids += int(id)
            # else:
            # print("valid", id)
    return invalids


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    aocd.submit(answer, part="a", day=2, year=2025)
