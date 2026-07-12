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
    total = 0
    for l in data.splitlines():
        lights, l = l.split("] ")
        buttons, power = l.split(" {")
        lights = [c == "#" for c in lights[1:]]
        buttons = [
            [int(i) for i in button[1:-1].split(",")] for button in buttons.split()
        ]
        power = [int(i) for i in power[:-1].split(",")]

        found = False
        for numbuttons in range(1, len(buttons) + 1):
            for combo in combinations(buttons, numbuttons):
                toggles = []
                for button in combo:
                    toggles.extend(button)
                cts = Counter(toggles)
                on = [cts[i] % 2 for i in range(len(lights))]
                if on == lights:
                    total += numbuttons
                    found = True
                    break
            if found:
                break
    return total


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    aocd.submit(answer, part="a", day=10, year=2025)
