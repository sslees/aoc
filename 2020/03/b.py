#! /bin/env python3

import math


def main():
    trees = []
    for dx, dy in (1, 1), (3, 1), (5, 1), (7, 1), (1, 2):
        with open("input.txt") as f:
            m = [l.strip() for l in f.readlines()]
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
    print(math.prod(trees))


if __name__ == "__main__":
    main()
