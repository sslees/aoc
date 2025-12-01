#! /usr/bin/env python3

from functools import cache

from utils.cells import VNEUMANN
from utils.grid import defaultgrid


@cache
def neighbors(p):
    return [tuple(map(sum, zip(p, d))) for d in VNEUMANN]


def area(grid, point):
    plant = grid[point]
    points = [point]
    good = set()
    while points:
        p = points.pop()
        good.add(p)
        for n in neighbors(p):
            if n not in points and n not in good and grid[n] == plant:
                points.append(n)
    return good


def perimiter(points):
    edges = set()
    for p in points:
        for n in neighbors(p):
            if n not in points:
                edges.add((p, n))
    return len(edges)


def solve(data: str):
    grid = defaultgrid(data)
    seen = set()
    score = 0
    for p in list(grid.keys()):
        if p not in seen:
            points = area(grid, p)
            seen.update(points)
            score += len(points) * perimiter(points)
    return score


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
