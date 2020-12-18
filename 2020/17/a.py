#! /bin/env python3

import copy
import itertools


def expand(cube):
    s = len(cube) + 2
    e = ["."] * s
    for slc in cube:
        for row in slc:
            row.insert(0, ".")
            row.append(".")
        slc.insert(0, e.copy())
        slc.append(e.copy())
    pad = [e.copy() for _ in range(s)]
    cube.insert(0, pad)
    cube.append(copy.deepcopy(pad))


def nxt(cube, z, y, x, sq):
    adj = []
    dirs = [d for d in itertools.product((-1, 0, 1), repeat=3) if d != (0, 0, 0)]
    for dz, dy, dx in dirs:
        try:
            adj.append(cube[z + dz][y + dy][x + dx])
        except IndexError:
            continue
    if sq == "#":
        return "#" if 2 <= adj.count("#") <= 3 else "."
    else:
        return "#" if adj.count("#") == 3 else "."


# def pretty(cube):
#     s = len(cube)
#     for z, slc in enumerate(cube):
#         print("z=", z - s // 2, sep="")
#         for r in slc:
#             print("".join(r))
#         print()


def main():
    with open("input.txt") as f:
        slc = [[c for c in l.strip()] for l in f.readlines()]
    s = len(slc)
    e = ["."] * s
    pad = [e.copy() for _ in range(s)]
    cube = [slc]
    cube.insert(0, pad)
    cube.append(copy.deepcopy(pad))

    for _ in range(5):  # why is this needed???
        expand(cube)

    for _ in range(6):
        expand(cube)
        tmp = [[["." for col in row] for row in slc] for slc in cube]
        for z, slc in enumerate(cube):
            for y, row in enumerate(slc):
                for x, col in enumerate(row):
                    tmp[z][y][x] = nxt(cube, z, y, x, col)
        cube = tmp
    print(len([col for slc in cube for row in slc for col in row if col == "#"]))


if __name__ == "__main__":
    main()
