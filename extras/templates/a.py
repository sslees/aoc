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
    # for i in [int(c) for c in data]:
    # for i in [int(s) for s in data.split(",")]:
    # for i in [int(l) for l in data.splitlines()]:
    # for c in data:
    # for s in data.split(","):
    for l in data.splitlines():
        # string_int_float = parse("{}, {:d}, {:f}", l)
        # print(string_int_float)
        pass
    return


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    # aocd.submit(answer, part="a", day=D, year=YYYY)
