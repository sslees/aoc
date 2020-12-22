#! /bin/env python3

import collections
import math


def main():
    hashes = {}  # would love a histogram for counts of values in a dict...
    with open("input.txt") as f:
        for piece in f.read()[:-1].removeprefix("Tile ").split("\n\nTile "):
            num, piece = piece.split(":\n")
            num, piece = int(num), piece.split("\n")
            hashes[num] = [
                hash(piece[0]),
                hash("".join((row[-1] for row in piece))),
                hash(piece[-1][::-1]),
                hash("".join((row[0] for row in piece[::-1]))),
                hash("".join((row[0] for row in piece))),
                hash(piece[-1]),
                hash("".join((row[-1] for row in piece[::-1]))),
                hash(piece[0][::-1]),
            ]
    cts = collections.Counter((h for p in hashes.values() for h in p))
    print(math.prod(p for p, hl in hashes.items() if sum(cts[h] for h in hl) == 12))


if __name__ == "__main__":
    main()
