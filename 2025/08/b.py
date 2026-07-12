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
    pairs = sorted(combinations(nets, 2), key=dist)
    for a, b in pairs:
        if len(Counter(nets.values())) == 2 and nets[a] != nets[b]:
            return a[0] * b[0]
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


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    aocd.submit(answer, part="b", day=8, year=2025)
