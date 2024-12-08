from collections import defaultdict


def defaultgrid(data: str, default=type(None)):
    grid = defaultdict(default)
    for y, line in enumerate(data.splitlines()):
        for x, c in enumerate(line):
            grid[x, y] = c
    return grid


def dimensions(data: str):
    lines = data.splitlines()
    return len(lines[0]), len(lines)
