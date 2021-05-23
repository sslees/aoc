#! /usr/bin/env python3

from collections import namedtuple
import math


def visible(loc, locs):
    angles = set()
    for l in locs - {loc}:
        angles.add(math.atan2(l.y - loc.y, l.x - loc.x))
    return len(angles)


def main():
    with open("input.txt") as f:
        data = [l.strip() for l in f.readlines()]
    locs = set()
    Loc = namedtuple("Loc", ("x", "y"))
    for r, line in enumerate(data):
        for c, char in enumerate(line):
            if char == "#":
                locs.add(Loc(c, -r))
    station = max(locs, key=lambda l: visible(l, locs))
    print(visible(station, locs))


if __name__ == "__main__":
    main()
