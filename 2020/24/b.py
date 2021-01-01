#! /bin/env python3

import collections
import itertools
import re

# aka neighborhood...
DIRS_HEX2D = [(x, y) for x, y in itertools.product((-1, 0, 1), repeat=2) if x != y]


def nbrs2d(cells, x, y, dirs=DIRS_HEX2D):
    return {(n := (x + dx, y + dy)): cells[n] for dx, dy in dirs}
    # [cells[*map(sum, zip(p, d))] for d in dirs]


def tf(cells, pos, state):
    ct = list(nbrs2d(cells, *pos).values()).count(True)
    return ct in (1, 2) if state else ct == 2


def sim(cells):
    cells |= {p: tf(cells, p, s) for p, s in list(cells.items())}


def pop(cells):
    return list(cells.values()).count(True)


# def pretty2dh(cells):
#     xs, ys = zip(*cells)
#     print(
#         "\n".join(
#             " " * (y - min(ys))
#             + "".join(
#                 ("#" if cells[x, y] else ".") + (" " if x or y else ")")
#                 for x in range(min(xs), max(xs) + 1)
#             ).rstrip()
#             for y in range(max(ys), min(ys) - 1, -1)
#         )
#         + "\n"
#     )


def main():
    with open("input.txt") as f:
        data = [l.strip() for l in f.readlines()]
    cells = collections.defaultdict(bool)
    for l in data:
        x, y = 0, 0
        for d in re.findall(r"[ns]?[ew]", l.replace("nw", "new").replace("se", "swe")):
            if d == "e":
                x += 1
            elif d == "w":
                x -= 1
            elif d == "ne":
                y += 1
            else:  # d == "sw"
                y -= 1
        cells[x, y] ^= True
    for p in list(cells.keys()):
        cells |= nbrs2d(cells, *p)
    for _ in range(100):
        sim(cells)
    print(pop(cells))


if __name__ == "__main__":
    main()
