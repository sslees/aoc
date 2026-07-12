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


def area(pair):
    (ax, ay), (bx, by) = pair
    return (abs(bx - ax) + 1) * (abs(by - ay) + 1)


def solve(data: str):
    corners = [tuple(parse("{:d},{:d}", l)) for l in data.splitlines()]
    # print(corners)
    # for pair in combinations(corners, 2):
    #     print(pair, area(pair))
    return max(area(pair) for pair in combinations(corners, 2))


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    aocd.submit(answer, part="a", day=9, year=2025)
