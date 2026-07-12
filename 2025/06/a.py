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
)

import aocd

# import networkx as nx
from parse import parse


def solve(data: str):
    a, b, c, d, o = data.splitlines()
    total = 0
    for na, nb, nc, nd, no in zip(
        a.split(), b.split(), c.split(), d.split(), o.split()
    ):
        if no == "+":
            total += int(na) + int(nb) + int(nc) + int(nd)
        else:
            total += int(na) * int(nb) * int(nc) * int(nd)
    return total


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    aocd.submit(answer, part="a", day=6, year=2025)
