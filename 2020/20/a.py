#! /bin/env python3

import collections
import math


def opts(tile):
    for _ in range(2):
        for _ in range(4):
            yield tile
            tile[:] = map("".join, zip(*reversed(tile)))  # rotate
        tile[:] = map("".join, zip(*tile))  # transpose


def main():
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    nbrs = collections.defaultdict(set)
    for o in data.split("\n\n"):
        num = int(o[5:9])
        tile = o[11:].split("\n")
        for o in opts(tile):
            nbrs[o[0]].add(num)
    cts = collections.Counter(p for e in nbrs.values() if len(e) > 1 for p in e)
    print(math.prod(e for e in cts if cts[e] == 4))


if __name__ == "__main__":
    main()
