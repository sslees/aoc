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
        buttonct = len(buttons)

        value = [0 for _ in target]
        presses = []
        # print("target", target)
        while True:
            print("value", value)
            button = buttons[len(presses)]
            # print("button", button)
            press = most(button, value, target)
            # print("most", press)
            presses.append(press)
            # print("presses", presses)
            if press:
                add(value, button, press)
            if len(presses) == buttonct:
                if value == target:
                    print("row answer", sum(presses))
                    total += sum(presses)
                    break
                else:
                    diff = [t - v for v, t in zip(value, target)]
                    print("backtracking...", diff)
                    add(value, buttons[-1], -presses[-1])
                    presses.pop()
                    while presses[-1] == 0:
                        presses.pop()
                    presses[-1] -= 1
                    # print("presses", presses)
                    add(value, buttons[len(presses) - 1], -1)
    return total + 1


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    # aocd.submit(answer, part="b", day=10, year=2025)
