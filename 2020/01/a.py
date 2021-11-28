#! /bin/env python3

from itertools import combinations


def solve(data: str):
    for a, b in combinations(data.splitlines(), 2):
        a = int(a)
        b = int(b)
        if a + b == 2020:
            return a * b


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
