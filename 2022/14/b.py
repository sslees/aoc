#! /usr/bin/env python3

from collections import defaultdict

import aocd


def solve(data: str):
    scan = defaultdict(bool)
    for l in data.splitlines():
        pts = [tuple(map(int, p.split(","))) for p in l.split(" -> ")]
        for i in range(len(pts) - 1):
            (x1, y1), (x2, y2) = pts[i], pts[i + 1]
            if x1 == x2:
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    scan[x1, y] = True
            elif y1 == y2:
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    scan[x, y1] = True
    ymax = max(y for _, y in scan)
    ct = 0
    while True:
        x, y = 500, 0
        while True:
            if scan[x, y]:
                return ct
            if y > ymax:
                scan[x, y] = True
                ct += 1
                break
            if not scan[x, y + 1]:
                x, y = x, y + 1
            elif not scan[x - 1, y + 1]:
                x, y = x - 1, y + 1
            elif not scan[x + 1, y + 1]:
                x, y = x + 1, y + 1
            else:
                scan[x, y] = True
                ct += 1
                break


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    aocd.submit(answer, part="b", day=14, year=2022)
