#! /usr/bin/env python3

from itertools import combinations, count
from parse import parse


def solve(data: str):
    return 0  # TODO
    data = data.splitlines()
    moons = [(list(parse("<x={:d}, y={:d}, z={:d}>", l)), [0, 0, 0]) for l in data]
    hist = [({tuple(p): 0}, {tuple(v): 0}) for p, v in moons]
    for t in count():
        for (p1, v1), (p2, v2) in combinations(moons, 2):
            for i in range(3):
                v1[i] = v1[i] + (1 if p1[i] < p2[i] else -1 if p1[i] > p2[i] else 0)
                v2[i] = v2[i] + (1 if p2[i] < p1[i] else -1 if p2[i] > p1[i] else 0)
        for i, (p, v) in enumerate(moons):
            p[:] = map(sum, zip(p, v))
            p, v = tuple(p), tuple(v)
            ph, vh = hist[i]
            if p in ph:
                print(f"moon {i} repeated pos {p} at time {t} after {t - ph[p]} steps")
            if v in vh:
                print(f"moon {i} repeated vel {v} at time {t} after {t - vh[v]} steps")
            ph[p] = vh[v] = t


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
