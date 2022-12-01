#! /usr/bin/env python3

import math
import random
import re
import statistics
from collections import Counter, defaultdict, deque, namedtuple
from functools import cache
from itertools import combinations, count, cycle, permutations, product, repeat

import aocd
from parse import parse


def solve(data: str):
    ct = 0
    for l in data.splitlines():
        sig, disp = l.split(" | ")
        sigs = sig.split()
        disps = disp.split()
        key = {}
        for s in sigs:
            ct = len(s)
            if ct == 2:
                key[1] = set(s)
            elif ct == 4:
                key[4] = set(s)
            elif ct == 3:
                key[7] = set(s)
            elif ct == 7:
                key[8] = set(s)
        key["a"] = key[7] - key[1]
    return ct


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    # aocd.submit(answer, part="b", day=8, year=2021)
