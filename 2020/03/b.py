#! /usr/bin/env python3

import math


def solve(data: str):
    trees = []
    for dx, dy in (1, 1), (3, 1), (5, 1), (7, 1), (1, 2):
        m = data.splitlines()
        x = 0
        y = 0
        mx = len(m[1])
        my = len(m)
        count = 0
        while y < my:
            if m[y][x] == "#":
                count += 1
            x += dx
            x = x % mx
            y += dy
        trees.append(count)
    return math.prod(trees)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
