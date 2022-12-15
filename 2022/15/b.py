#! /usr/bin/env python3

import aocd
from parse import parse

MAX = 4_000_000


def manhattan(sx, sy, bx, by):
    return abs(sx - bx) + abs(sy - by)


def solve(data: str):
    sensors = []
    for l in data.splitlines():
        sx, sy, bx, by = parse(
            "Sensor at x={:d}, y={:d}: closest beacon is at x={:d}, y={:d}", l
        )
        sensors.append((sx, sy, manhattan(sx, sy, bx, by)))
    x = y = 0
    for y in range(MAX + 1):
        while x <= MAX:
            kicked = False
            for sx, sy, d in sensors:
                if manhattan(sx, sy, x, y) <= d:
                    dy = abs(sy - y)
                    x = sx + d - dy + 1
                    kicked = True
                    break
            if not kicked:
                return x * 4_000_000 + y
        x = 0


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    aocd.submit(answer, part="b", day=15, year=2022)
