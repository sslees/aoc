#! /usr/bin/env python3

import math
import random
import re
import statistics
from collections import Counter, defaultdict, deque, namedtuple
from functools import cache
from itertools import (
    combinations,
    count,
    cycle,
    pairwise,
    permutations,
    product,
    repeat,
    zip_longest,
)

import aocd

from parse import parse


def vertical(pair):
    (ax, _), (bx, _) = pair
    return ax == bx


def connect(pair):
    (ax, ay), (bx, by) = pair
    if ax == bx:
        if by > ay:
            return [(ax, y) for y in range(ay + 1, by)]
        else:
            return [(ax, y) for y in range(by + 1, ay)]
    if ay == by:
        if bx > ax:
            return [(x, ay) for x in range(ax + 1, bx)]
        else:
            return [(x, ay) for x in range(bx + 1, ax)]


def area(pair):
    (ax, ay), (bx, by) = pair
    return (abs(bx - ax) + 1) * (abs(by - ay) + 1)


def corners(pair):
    (ax, ay), (bx, by) = pair
    return [(ax, ay), (bx, by), (ax, by), (bx, ay)]


def midpt(pair):
    (ax, ay), (bx, by) = pair
    return (ax + bx) // 2, (ay + by) // 2


def checkpt(point, reds, vgreens, hgreens):
    cx, cy = point
    return (
        (cx, cy) in reds
        or (cx, cy) in vgreens
        or (cx, cy) in hgreens
        or (
            (
                sum(1 for x, y in vgreens if x >= cx and y == cy) % 2 == 1
                or (
                    sum(1 for x, y in reds if x >= cx and y == cy) > 0
                    and sum(1 for x, y in reds if x >= cx and y == cy) % 2 == 0
                )
            )
            and (
                sum(1 for x, y in vgreens if x <= cx and y == cy) % 2 == 1
                or (
                    sum(1 for x, y in reds if x <= cx and y == cy) > 0
                    and sum(1 for x, y in reds if x <= cx and y == cy) % 2 == 0
                )
            )
            and (
                sum(1 for x, y in hgreens if y >= cy and x == cx) % 2 == 1
                or (
                    sum(1 for x, y in reds if y >= cy and x == cx) > 0
                    and sum(1 for x, y in reds if y >= cy and x == cx) % 2 == 0
                )
            )
            and (
                sum(1 for x, y in hgreens if y <= cy and x == cx) % 2 == 1
                or (
                    sum(1 for x, y in reds if y <= cy and x == cx) > 0
                    and sum(1 for x, y in reds if y <= cy and x == cx) % 2 == 0
                )
            )
        )
    )


def checkcorners(pair, reds, vgreens, hgreens):
    return all(checkpt((cx, cy), reds, vgreens, hgreens) for cx, cy in corners(pair))


def checkedges(pair, reds, vgreens, hgreens):
    if not checkpt(midpt(pair), reds, vgreens, hgreens):
        return False
    (ax, ay), (bx, by) = pair
    minx = min(ax, bx)
    miny = min(ay, by)
    maxx = max(ax, bx)
    maxy = max(ay, by)
    if any(True for x, y in reds if minx < x < maxx and miny < y < maxy):
        return False
    # TODO: don't check every green!
    if any(True for x, y in vgreens if minx < x < maxx and miny < y < maxy):
        return False
    if any(True for x, y in hgreens if minx < x < maxx and miny < y < maxy):
        return False
    return True


def solve(data: str):
    reds = [tuple(parse("{:d},{:d}", l)) for l in data.splitlines()]
    vgreens = []
    hgreens = []
    for pair in pairwise(reds + [reds[0]]):
        if vertical(pair):
            vgreens.extend(connect(pair))
        else:
            hgreens.extend(connect(pair))
    for pair in sorted(combinations(reds, 2), key=area, reverse=True):
        if checkcorners(pair, reds, vgreens, hgreens):
            if checkedges(pair, reds, vgreens, hgreens):
                return area(pair)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    aocd.submit(answer, part="b", day=9, year=2025)
