#! /usr/bin/env python3

from itertools import combinations
from string import ascii_letters, digits

from utils.grid import defaultgrid


def solve(data: str):
    grid = defaultgrid(data)
    antinodes = set()
    for freq in digits + ascii_letters:
        antennas = [p for p, f in grid.items() if f == freq]
        for (ax, ay), (bx, by) in combinations(antennas, r=2):
            dx, dy = bx - ax, by - ay
            for n in range(min(abs(dx), abs(dy)), 0, -1):
                if dx % n == 0 and dy % n == 0:
                    dx, dy = dx / n, dy / n
            n = 0
            while grid[p := (ax - (dx * n), ay - (dy * n))] is not None:
                antinodes.add(p)
                n += 1
            n = 1
            while grid[p := (ax + (dx * n), ay + (dy * n))] is not None:
                antinodes.add(p)
                n += 1
    return len(antinodes)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
