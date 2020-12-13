#! /usr/bin/env python3

from functools import partial
from itertools import combinations


def colinear(s, a, b):
    dya = a[1] - s[1]
    dyb = b[1] - s[1]
    dxa = a[0] - s[0]
    dxb = b[0] - s[0]

    return dya * dxb == dyb * dxa and \
        (dyb > 0 if dya > 0 else dyb <= 0) and \
        (dxb > 0 if dxa > 0 else dxb <= 0)


def visible(station, asteroids):
    vis = asteroids - {station}
    for a, b, in combinations(asteroids - {station}, 2):
        if b in vis and colinear(station, a, b):
            vis.remove(b)

    return len(vis)


def main():
    asteroids = set()
    with open('input.txt') as f:
        for y, line in enumerate(f.readlines()):
            for x, char in enumerate(line.strip()):
                if char == '#':
                    asteroids.add((x, y))
    station = max(asteroids, key=partial(visible, asteroids=asteroids))
    print('{} @ {}'.format(visible(station, asteroids), station))


if __name__ == '__main__':
    main()
