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


@cache
def dist(pair):
    (ax, ay, az), (bx, by, bz) = pair
    return ((bx - ax) ** 2 + (by - ay) ** 2 + (bz - az) ** 2) ** 0.5


def size(net, nets):
    return len([p for p in nets if nets[p] == net])


def solve(data: str):
    nets = {
        tuple(parse("{:d},{:d},{:d}", l)): i for i, l in enumerate(data.splitlines())
    }
    turns = 10 if len(nets) < 100 else 1000
    for a, b in sorted(combinations(nets, 2), key=dist)[:turns]:
        na = nets[a]
        nb = nets[b]
        if size(a, nets) > size(b, nets):
            for p in nets:
                if nets[p] == nb:
                    nets[p] = na
        else:
            for p in nets:
                if nets[p] == na:
                    nets[p] = nb
    # print(Counter(nets.values()).most_common())
    return math.prod([s for _, s in Counter(nets.values()).most_common(3)])


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    # aocd.submit(answer, part="a", day=8, year=2025)
