#! /usr/bin/env python3

import aocd


def score(i: str):
    return ord(i) - ord("A") + 27 if i.isupper() else ord(i) - ord("a") + 1


def solve(data: str):
    val = 0
    for l in data.splitlines():
        ct = len(l) // 2
        for i in set(l[:ct]) & set(l[ct:]):
            val += score(i)
    return val


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    aocd.submit(answer, part="a", day=3, year=2022)
