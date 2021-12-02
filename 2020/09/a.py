#! /usr/bin/env python3

from itertools import combinations


def solve(data: str):
    d = [int(l) for l in data.splitlines()]
    pre = 25
    for i in range(pre, len(d)):
        if not any(
            [a != b and a + b == d[i] for a, b in combinations(d[i - pre : i], 2)]
        ):
            return d[i]
            break


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
