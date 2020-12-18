#! /bin/env python3

import copy
import itertools


def expand(hcube):
    s = len(hcube) + 2
    e = ["."] * s
    pad = [e.copy() for _ in range(s)]
    for cube in hcube:
        for slc in cube:
            for row in slc:
                row.insert(0, ".")
                row.append(".")
            slc.insert(0, e.copy())
            slc.append(e.copy())
        cube.insert(0, copy.deepcopy(pad))
        cube.append(copy.deepcopy(pad))
    hpad = [copy.deepcopy(pad) for _ in range(s)]
    hcube.insert(0, hpad)
    hcube.append(copy.deepcopy(hpad))


def nxt(hcube, w, z, y, x, sq):
    adj = []
    dirs = [d for d in itertools.product((-1, 0, 1), repeat=4) if d != (0, 0, 0, 0)]
    for dw, dz, dy, dx in dirs:
        try:
            adj.append(hcube[w + dw][z + dz][y + dy][x + dx])
        except IndexError:
            continue
    if sq == "#":
        return "#" if 2 <= adj.count("#") <= 3 else "."
    else:
        return "#" if adj.count("#") == 3 else "."


# def pretty(hcube):
#     half = len(hcube) // 2
#     for w, cube in enumerate(hcube):
#         for z, slc in enumerate(cube):
#             print("z={}, w={}".format(z - half, w - half))
#             for r in slc:
#                 print("".join(r))
#             print()


def main():
    with open("input.txt") as f:
        slc = [[c for c in l.strip()] for l in f.readlines()]
    s = len(slc)
    e = ["."] * s
    pad = [e.copy() for _ in range(s)]
    cube = [slc]
    cube.insert(0, pad)
    cube.append(copy.deepcopy(pad))
    hpad = [copy.deepcopy(pad) for _ in range(s)]
    hcube = [cube]
    hcube.insert(0, hpad)
    hcube.append(copy.deepcopy(hpad))

    for _ in range(6):  # why is this needed???
        expand(hcube)

    for _ in range(6):
        expand(hcube)
        tmp = [
            [[["." for col in row] for row in slc] for slc in cube] for cube in hcube
        ]
        for w, cube in enumerate(hcube):
            for z, slc in enumerate(cube):
                for y, row in enumerate(slc):
                    for x, col in enumerate(row):
                        tmp[w][z][y][x] = nxt(hcube, w, z, y, x, col)
        hcube = tmp
    print(
        len(
            [
                col
                for cube in hcube
                for slc in cube
                for row in slc
                for col in row
                if col == "#"
            ]
        )
    )


if __name__ == "__main__":
    main()
