#! /bin/env python3

from collections import defaultdict
import math
import re


def main():
    with open("input.txt") as f:
        notes = f.read().rstrip("\r\n")
    rules = {}
    for bound in re.findall(r"(?:\w|[ ])+:[^\n]+", notes):
        name, rule = bound.split(": ")
        a, b = rule.split(" or ")
        a1, a2 = a.split("-")
        b1, b2 = b.split("-")
        a1, a2, b1, b2 = int(a1), int(a2), int(b1), int(b2)
        rules[name] = (
            lambda v=None, a1=a1, a2=a2, b1=b1, b2=b2: a1 <= v <= a2 or b1 <= v <= b2
        )

    mine = re.search(r"your ticket:\n(\d+[,\n])+", notes).group(0)
    mine = list(map(int, re.findall(r"\d+", mine)))

    nearby = re.search(r"nearby tickets:\n(\d+[,\n]?)+", notes).group(0)
    nearby = nearby.removeprefix("nearby tickets:\n").strip().split("\n")
    nearby = (list(map(int, n.split(","))) for n in nearby)
    nearby = [
        nb for nb in nearby if all((any((r(v) for r in rules.values())) for v in nb))
    ]

    candidates = defaultdict(set)
    for name, rule in rules.items():
        for c in range(len(nearby[0])):
            col = [nb[c] for nb in nearby]
            if all((rule(v) for v in col)):
                candidates[name].add(c)
    taken = set()
    for name, pos in sorted(candidates.items(), key=lambda c: len(c[1])):
        candidates[name] = pos - taken
        taken.update(candidates[name])
    fields = (mine[next(iter(v))] for k, v in candidates.items() if "departure" in k)
    print(math.prod(fields))


if __name__ == "__main__":
    main()
