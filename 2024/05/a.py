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
    rulestr, updatestr = data.split("\n\n")
    rules = []
    for rule in rulestr.splitlines():
        first, second = rule.split("|")
        rules.append((int(first), int(second)))
    # print(rules)
    # print("rules len", len(rules))

    score = 0
    for update in updatestr.splitlines():
        pages = [int(s) for s in update.split(",")]
        bad = False
        for a, b in rules:
            if a in pages and b in pages:
                if pages.index(a) >= pages.index(b):
                    # print("bad", pages)
                    bad = True
                    break
        if not bad:
            score += pages[len(pages) // 2]

    return score


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    # print(answer)
    aocd.submit(answer, part="a", day=5, year=2024)
