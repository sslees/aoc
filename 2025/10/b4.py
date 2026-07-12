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


def pretty(value, target):
    lines = [
        "." * min(v, t) + ("#" if t > v else "!") * abs(t - v)
        for v, t in zip(value, target)
    ]
    print("\n".join(reversed(list(map("".join, zip_longest(*lines, fillvalue=" "))))))
    print()


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
        orig_target = target  # prob should decrement from target

        print("starting line:", l)

        seen = set()

        pretty(target, orig_target)

        stack: list[list] = []
        while True:
            order = list(ordered(buttons, tuple(target)))
            stack.append(order)
            if len(order) == 0:
                print("backtracking")
                while len(stack[-1]) == 0:
                    stack.pop()
                    target = add(tuple(target), stack[-1].pop())
                target = sub(tuple(target), stack[-1][-1])
                continue
            best = order[-1]
            target = sub(tuple(target), best)
            if tuple(target) in seen:
                stack.append([])  # simulate no options on next turn
                while len(stack[-1]) == 0:
                    stack.pop()
                    target = add(tuple(target), stack[-1].pop())
            else:
                seen.add(tuple(target))
            pretty(target, orig_target)
            if all(t == 0 for t in target):
                print("answer:", len(stack))
                total += len(stack)
                break
    print("total:", total)
    return total


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    #     data = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
    # [...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
    # [.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""
    answer = solve(data)
    print(answer)
    # aocd.submit(answer, part="b", day=10, year=2025)
