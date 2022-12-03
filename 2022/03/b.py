#! /usr/bin/env python3

import aocd
from more_itertools import grouper


def score(i: str):
    return ord(i) - ord("A") + 27 if i.isupper() else ord(i) - ord("a") + 1


def solve(data: str):
    val = 0
    for a, b, c in grouper(data.splitlines(), 3):
        for i in set(a) & set(b) & set(c):
            val += score(i)
    return val


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    aocd.submit(answer, part="b", day=3, year=2022)
