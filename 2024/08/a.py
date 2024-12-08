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
            antinode1 = (ax - dx, ay - dy)
            antinode2 = (bx + dx, by + dy)
            if grid[antinode1] is not None:
                antinodes.add(antinode1)
            if grid[antinode2] is not None:
                antinodes.add(antinode2)
    return len(antinodes)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
