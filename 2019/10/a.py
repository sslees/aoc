#! /usr/bin/env python3

import math
from collections import namedtuple


def visible(loc, locs):
    angles = set()
    for l in locs - {loc}:
        angles.add(math.atan2(l.y - loc.y, l.x - loc.x))
    return len(angles)


def solve(data: str):
    data = data.splitlines()
    locs = set()
    Loc = namedtuple("Loc", ("x", "y"))
    for r, line in enumerate(data):
        for c, char in enumerate(line):
            if char == "#":
                locs.add(Loc(c, -r))
    station = max(locs, key=lambda l: visible(l, locs))
    return visible(station, locs)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
