#! /usr/bin/env python3

import math
from operator import sub
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


def most(button, value, target):
    diff = [t - v for v, t in zip(value, target)]
    return min(d for b, d in zip(button, diff) if b)


def add(value, button, n):
    diff = [b * n for b in button]
    value[:] = [v + d for v, d in zip(value, diff)]


def solve(data: str):
    total = 0
    for l in data.splitlines():
        buttons, target = l.split("] ")[1].split(" {")
        target = [int(i) for i in target[:-1].split(",")]
        buttons = [[int(i) for i in b[1:-1].split(",")] for b in buttons.split()]
        # buttons = sorted(buttons, key=len, reverse=True)
        buttons = [[int(c in b) for c in range(len(target))] for b in buttons]

        print(f"starting line with {math.perm(len(buttons))} perms")
        for order in permutations(buttons):
            # score = [sum(b) for b in order]
            # if score != sorted(score, reverse=True):
            #     continue
            value = [0 for _ in target]
            presses = 0
            debug = {}
            for b in order:
                m = most(b, value, target)
                add(value, b, m)
                presses += m
                debug[str(b)] = m
            if value == target:
                total += presses
                print("debug", presses, debug)
                break
        print("failed")

    return total


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    # aocd.submit(answer, part="b", day=10, year=2025)
