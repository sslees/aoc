#! /usr/bin/env python3

from itertools import combinations


def solve(data: str):
    d = [int(l) for l in data.splitlines()]
    pre = 25
    for i in range(pre, len(d)):
        if not any(
            [a != b and a + b == d[i] for a, b in combinations(d[i - pre : i], 2)]
        ):
            target = d[i]
            break
    for n in range(2, len(d) + 1):
        for i in range(len(d) - n + 1):
            seq = d[i : i + n]
            if sum(seq) == target:
                return min(seq) + max(seq)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
