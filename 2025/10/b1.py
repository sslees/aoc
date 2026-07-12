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


@cache
def add(target, button):
    return [t + d for t, d in zip(target, button)]


@cache
def sub(target, button):
    return [t - d for t, d in zip(target, button)]


@cache
def score(button, target):
    points = [t for b, t in zip(button, target) if b]
    return sum(points) if 0 not in points else 0


@cache
def ordered(buttons, target):
    return [
        b for b in sorted(buttons, key=lambda b: score(b, target)) if score(b, target)
    ]


def solve(data: str):
    total = 0
    for l in data.splitlines():
        mappings, target = l.split("] ")[1].split(" {")
        target = [int(i) for i in target[:-1].split(",")]
        mappings = reversed(
            [[int(i) for i in b[1:-1].split(",")] for b in mappings.split()]
        )
        buttons = tuple(
            tuple(int(c in b) for c in range(len(target))) for b in mappings
        )

        print("starting line:", l)

        stack: list[list] = []
        while True:
            order = list(ordered(buttons, tuple(target)))
            stack.append(order)
            if len(order) == 0:
                while len(stack[-1]) == 0:
                    # print("popping empty list...")
                    stack.pop()
                    # print("popping exhausted button...")
                    target = add(tuple(target), stack[-1].pop())
                target = sub(tuple(target), stack[-1][-1])
                continue
            best = order[-1]
            # print("best", best)
            target = sub(tuple(target), best)
            if all(t == 0 for t in target):
                print("answer:", len(stack))
                total += len(stack)
                break
    print("total:", total)
    return total


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    # aocd.submit(answer, part="b", day=10, year=2025)
