#! /usr/bin/env python3

import re
from collections import defaultdict


def solve(data: str):
    data = data.splitlines()
    tiles = defaultdict(bool)
    for l in data:
        ds = re.findall(r"[ns]?[ew]", l.replace("nw", "new").replace("se", "swe"))
        tiles[ds.count("e") - ds.count("w"), ds.count("ne") - ds.count("sw")] ^= True
    return list(tiles.values()).count(True)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
