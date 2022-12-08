#! /usr/bin/env python3

import aocd


def solve(data: str):
    grid = [list(map(int, l)) for l in data.splitlines()]
    w = len(grid[0])
    h = len(grid)
    vis = set()
    for c in range(1, w - 1):
        m = 0
        for r in range(1, h - 1):
            m = max(m, grid[r - 1][c])
            if grid[r][c] > m:
                vis.add((r, c))
    for c in range(1, w - 1):
        m = 0
        for r in range(h - 2, 0, -1):
            m = max(m, grid[r + 1][c])
            if grid[r][c] > m:
                vis.add((r, c))
    for r in range(1, h - 1):
        m = 0
        for c in range(1, w - 1):
            m = max(m, grid[r][c - 1])
            if grid[r][c] > m:
                vis.add((r, c))
    for r in range(1, h - 1):
        m = 0
        for c in range(w - 2, 0, -1):
            m = max(m, grid[r][c + 1])
            if grid[r][c] > m:
                vis.add((r, c))
    return len(vis) + (w + h) * 2 - 4


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    aocd.submit(answer, part="a", day=8, year=2022)
