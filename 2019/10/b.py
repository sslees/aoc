#! /usr/bin/env python3

from collections import defaultdict, namedtuple
import math


def visible(loc, locs):
    angles = set()
    for l in locs - {loc}:
        angles.add(math.atan2(l.y - loc.y, l.x - loc.x))
    return len(angles)


def dist(a, b):
    return ((b.x - a.x) ** 2 + (b.y - a.y) ** 2) ** 0.5


def ordered(station, locs):
    angles = defaultdict(list)
    for l in locs - {station}:
        angle = math.atan2(l.y - station.y, l.x - station.x)
        angles[(math.pi / 2 - angle) % (2 * math.pi)].append(l)
    order = {}
    for a, ls in angles.items():
        for i, l in enumerate(sorted(ls, key=lambda p: dist(station, p))):
            order[a + 2 * math.pi * i] = l
    return [order[o] for o in sorted(order)]


def main():
    with open("input.txt") as f:
        data = [l.strip() for l in f.readlines()]
    locs = set()
    Pt = namedtuple("Pt", ("x", "y"))
    for r, line in enumerate(data):
        for c, char in enumerate(line):
            if char == "#":
                locs.add(Pt(c, -r))
    station = max(locs, key=lambda l: visible(l, locs))
    winner = ordered(station, locs)[199]
    print(winner.x * 100 - winner.y)


if __name__ == "__main__":
    main()
