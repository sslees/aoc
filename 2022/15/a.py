#! /usr/bin/env python3

import aocd
from parse import parse

Y = 2_000_000


def manhattan(sx, sy, bx, by):
    return abs(sx - bx) + abs(sy - by)


def ignore(sx, sy, d):
    dy = abs(sy - Y)
    return set(range(sx - d + dy, sx + d - dy + 1))


def solve(data: str):
    sensors = set()
    beacons = set()
    ignored = set()
    for l in data.splitlines():
        sx, sy, bx, by = parse(
            "Sensor at x={:d}, y={:d}: closest beacon is at x={:d}, y={:d}", l
        )
        sensors.add((sx, sy))
        beacons.add((bx, by))
        d = manhattan(sx, sy, bx, by)
        ignored |= ignore(sx, sy, d)
    return len(
        ignored - {x for x, y in sensors if y == Y} - {x for x, y in beacons if y == Y}
    )


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    aocd.submit(answer, part="a", day=15, year=2022)
