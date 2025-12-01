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
import networkx as nx
from parse import parse


def solve(data: str):
    diskmap = deque(int(c) for c in data)
    fid = 0
    runlens = deque([(fid, diskmap.popleft())])
    while diskmap:
        runlens.append((-1, diskmap.popleft()))
        fid += 1
        runlens.append((fid, diskmap.popleft()))
    i = len(runlens) - 1
    while i > 0:
        if runlens[i][0] == -1:
            i -= 1
        else:
            for j in range(i):
                if runlens[j][0] == -1 and runlens[j][1] >= runlens[i][1]:
                    extra = runlens[j][1] - runlens[i][1]
                    runlens[j] = runlens[i]
                    runlens[i] = (-1, runlens[i][1])
                    if extra:
                        runlens.insert(j + 1, (-1, extra))
                        i += 1
                    break
            i -= 1
    cksum = 0
    block = 0
    while runlens:
        runlen = runlens.popleft()
        for _ in range(runlen[1]):
            if runlen[0] != -1:
                cksum += block * runlen[0]
            block += 1
    return cksum


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    # # aocd.submit(answer, part="b", day=9, year=2024)
