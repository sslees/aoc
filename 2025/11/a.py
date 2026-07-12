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

import networkx as nx
from parse import parse


def solve(data: str):
    g = nx.DiGraph()
    for l in data.splitlines():
        device, outputs = l.split(": ")
        for output in outputs.split():
            g.add_edge(device, output)
    return len(list(nx.all_simple_paths(g, "you", "out")))


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    aocd.submit(answer, part="a", day=11, year=2025)
