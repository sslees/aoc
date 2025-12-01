#! /usr/bin/env python3

import math
import random
import re
import statistics
from collections import Counter, defaultdict, deque, namedtuple
from functools import cache
from itertools import combinations, count, cycle, permutations, product, repeat

import aocd
import networkx as nx
from parse import parse


def solve(data: str):
    result = 0
    for l in data.splitlines():
        answer, origargs = l.split(": ")
        answer = int(answer)
        origargs = deque([int(o) for o in origargs.split()])
        for origops in product("+*|", repeat=len(origargs) - 1):
            args = origargs.copy()
            ops = deque(origops)
            a = args.popleft()
            while ops:
                op = ops.popleft()
                arg = args.popleft()
                if op == "+":
                    a += arg
                elif op == "*":
                    a *= arg
                elif op == "|":
                    a = int(str(a) + str(arg))
            if a == answer:
                result += answer
                break
    return result


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    # print(answer)
    aocd.submit(answer, part="b", day=7, year=2024)
