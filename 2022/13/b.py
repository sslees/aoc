#! /usr/bin/env python3

from functools import cmp_to_key

import aocd


def cmp(l, r):
    if type(l) == type(r) == int:
        return -1 if l < r else 1 if l > r else 0
    elif type(l) == type(r) == list:
        for l2, r2 in zip(l, r):
            if (c2 := cmp(l2, r2)) != 0:
                return c2
        return cmp(len(l), len(r))
    else:
        return cmp([l], r) if type(l) == int else cmp(l, [r])


def solve(data: str):
    d1 = [[2]]
    d2 = [[6]]
    pkts = sorted([eval(l) for l in data.split()] + [d1, d2], key=cmp_to_key(cmp))
    return (pkts.index(d1) + 1) * (pkts.index(d2) + 1)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    aocd.submit(answer, part="b", day=13, year=2022)
