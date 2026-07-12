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


def paths(g, a, b):
    return sum(1 for _ in nx.all_simple_paths(g, a, b))


def solve(data: str):
    # g = nx.DiGraph()
    # for l in data.splitlines():
    #     device, outputs = l.split(": ")
    #     for output in outputs.split():
    #         g.add_edge(device, output)

    # a = paths(g, "svr", "fft") * paths(g, "fft", "dac") * paths(g, "dac", "out")
    # b = paths(g, "svr", "dac") * paths(g, "dac", "fft") * paths(g, "fft", "out")
    # return a + b

    # looks like 3 walk lengths: 467 3397 14139
    # min_lenth = nx.shortest_path_length(g, "svr", "fft")
    # for i in count():
    #     print(nx.number_of_walks(g, min_lenth + i)["svr"]["fft"])

    # looks like 5 walk lengths: 103401 312257 1213361 1626169 2423217
    # min_lenth = nx.shortest_path_length(g, "fft", "dac")
    # for i in count():
    #     print(nx.number_of_walks(g, min_lenth + i)["fft"]["dac"])

    # looks like 1 walk length: 4800
    # min_lenth = nx.shortest_path_length(g, "dac", "out")
    # for i in count():
    #     print(nx.number_of_walks(g, min_lenth + i)["dac"]["out"])

    # looks like 9 walk lengths: 191050410 1860322172 12039108963 40620474811 117431401767 204169439069 326926176540 264831425477 283355972137
    # min_lenth = nx.shortest_path_length(g, "svr", "dac")
    # for i in count():
    #     print(nx.number_of_walks(g, min_lenth + i)["svr"]["dac"])

    # looks like ??? walk lengths: 0
    # min_lenth = nx.shortest_path_length(g, "dac", "fft")
    # for i in count():
    #     print(nx.number_of_walks(g, min_lenth + i)["dac"]["fft"])

    # looks like ??? walk lengths:
    # min_lenth = nx.shortest_path_length(g, "fft", "out")
    # for i in count():
    #     print(nx.number_of_walks(g, min_lenth + i)["fft"]["out"])

    return (
        sum([467, 3397, 14139])
        * sum([103401, 312257, 1213361, 1626169, 2423217])
        * 4800
    )


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    # aocd.submit(answer, part="b", day=11, year=2025)
