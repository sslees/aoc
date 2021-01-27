#! /usr/bin/env python3

from itertools import combinations
import math


def dist(s, a):
    dy = s[1] - a[1]
    dx = a[0] - s[0]

    return (dy ** 2 + dx ** 2) ** 0.5


def colinear(s, a, b):
    dya = s[1] - a[1]
    dyb = s[1] - b[1]
    dxa = a[0] - s[0]
    dxb = b[0] - s[0]

    return (
        dya * dxb == dyb * dxa
        and (dyb > 0 if dya > 0 else dyb <= 0)
        and (dxb > 0 if dxa > 0 else dxb <= 0)
    )


def visible(s, aa):
    vis = aa - {s}
    for a, b in combinations(aa - {s}, 2):
        f = max(a, b, key=lambda a: dist(s, a))
        if f in vis and colinear(s, a, b):
            vis.remove(f)

    return vis


def angle(s, a):
    dy = s[1] - a[1]
    dx = a[0] - s[0]
    angl = -math.degrees(math.atan(dy / dx if dx else float("inf")))
    angl = angl + 180 if dx < 0 or dx == 0 and dy < 0 else angl

    return angl + 90


def main():
    aa = set()
    with open("input.txt") as f:
        for y, line in enumerate(f.readlines()):
            for x, char in enumerate(line.strip()):
                if char == "#":
                    aa.add((x, y))
    s = max(aa, key=lambda a: len(visible(a, aa)))
    a = sorted(visible(s, aa), key=lambda a: angle(s, a))[199]
    print(a[0] * 100 + a[1])


if __name__ == "__main__":
    main()
