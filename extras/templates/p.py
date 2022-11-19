#! /usr/bin/env python3

import math
import random
import re
from collections import Counter, defaultdict, deque, namedtuple
from functools import cache
from itertools import combinations, count, cycle, permutations, product, repeat

import aocd
from parse import parse


def solve(data: str):
    [int(c) for c in data]
    [int(l) for l in data.splitlines()]
    [int(s) for s in data.split(",")]

    for l in data.splitlines():
        print(l)
    return 0


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    # aocd.submit(answer, part="p", day=d, year=yyyy)
