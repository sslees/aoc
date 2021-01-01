#! /bin/env python3

import collections
import re


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
    print(list(cells.values()).count(True))


if __name__ == "__main__":
    main()
