#! /usr/bin/env python3

from itertools import product

from utils.grid import defaultgrid

DIRS = [p for p in product((-1, 0, 1), repeat=2) if any(p)]


def solve(data: str):
    grid = defaultgrid(data, str)
    ct = 0
    for (x, y), c in list(grid.items()):
        if c == "X":
            for dx, dy in DIRS:
                if "".join(grid[x + dx * n, y + dy * n] for n in range(1, 4)) == "MAS":
                    ct += 1
    return ct


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
