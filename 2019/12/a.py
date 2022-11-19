#! /usr/bin/env python3

from itertools import combinations

from parse import parse


def solve(data: str):
    data = data.splitlines()
    moons = [(list(parse("<x={:d}, y={:d}, z={:d}>", l)), [0, 0, 0]) for l in data]
    for _ in range(1_000):
        for (p1, v1), (p2, v2) in combinations(moons, 2):
            for i in range(3):
                v1[i] = v1[i] + (1 if p1[i] < p2[i] else -1 if p1[i] > p2[i] else 0)
                v2[i] = v2[i] + (1 if p2[i] < p1[i] else -1 if p2[i] > p1[i] else 0)
        for p, v in moons:
            p[:] = map(sum, zip(p, v))
    return sum(sum(map(abs, p)) * sum(map(abs, v)) for p, v in moons)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
