#! /usr/bin/env python3

from collections import Counter
from itertools import product

from utils.grid import defaultgrid

DIRS = [p for p in product((-1, 0, 1), repeat=2) if all(p)]


def solve(data: str):
    grid = defaultgrid(data, str)
    centers = Counter()
    for (x, y), c in list(grid.items()):
        if c == "M":
            for dx, dy in DIRS:
                if "".join(grid[x + dx * n, y + dy * n] for n in range(1, 3)) == "AS":
                    centers[x + dx, y + dy] += 1
    return len([p for p in centers.keys() if centers[p] == 2])


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
