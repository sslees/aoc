#! /usr/bin/env python3

from functools import cache


@cache
def change(n):
    if n == 0:
        return [1]
    elif len(str(n)) % 2 == 0:
        s = str(n)
        l = len(s)
        return [int(s[: l // 2]), int(s[l // 2 :])]
    else:
        return [n * 2024]


@cache
def evolve(n, t):
    return 1 if t == 0 else sum(evolve(n2, t - 1) for n2 in change(n))


def solve(data: str):
    return sum(evolve(n, 25) for n in [int(s) for s in data.split()])


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
