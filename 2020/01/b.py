#! /bin/env python3

from itertools import combinations


def solve(data: str):
    for a, b, c in combinations(data.splitlines(), 3):
        a = int(a)
        b = int(b)
        c = int(c)
        if a + b + c == 2020:
            return a * b * c


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
