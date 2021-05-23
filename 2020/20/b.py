#! /bin/env python3

from collections import Counter, defaultdict
import math

MONSTER = [
    "                  # ",
    "#    ##    ##    ###",
    " #  #  #  #  #  #   ",
]


def opts(tile):
    for _ in range(2):
        for _ in range(4):
            yield tile
            tile[:] = map("".join, zip(*reversed(tile)))  # rotate
        tile[:] = map("".join, zip(*tile))  # transpose


def stitch(tiles, puzzle):
    lines = []
    for r in puzzle:
        r = [[s[1:-1] for s in tiles[n][1:-1]] for n in r]
        lines.extend(map("".join, zip(*r)))
    return lines


def main():
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    tiles = {}
    nbrs = defaultdict(set)
    for t in data.split("\n\n"):
        num = int(t[5:9])
        tile = t[11:].split("\n")
        tiles[num] = tile
        for o in opts(tile):
            nbrs[o[0]].add(num)
    cts = Counter(p for e in nbrs.values() if len(e) > 1 for p in e)
    rct = int(math.sqrt(len(tiles)))
    puzzle = [[0] * rct for _ in range(rct)]
    for r in range(rct):
        for c in range(rct):
            if r == c == 0:  # orient an upper left corner
                cur = next(e for e in cts if cts[e] == 4)
                any(
                    len(nbrs[o[0]]) == len(nbrs["".join((r[0] for r in o[::-1]))]) == 1
                    for o in opts(tiles[cur])
                )
            elif c == 0:  # align top edge with bottom edge of piece above
                cur = puzzle[r - 1][0]
                edge = tiles[cur][-1]
                cur = next(p for p in nbrs[edge] if p != cur)
                any(o[0] == edge for o in opts(tiles[cur]))
            else:  # align left edge with right edge of previous piece
                edge = "".join((r[-1] for r in tiles[cur]))
                cur = next(p for p in nbrs[edge] if p != cur)
                any("".join((r[0] for r in o)) == edge for o in opts(tiles[cur]))
            puzzle[r][c] = cur
    stitched = stitch(tiles, puzzle)
    checks = {
        (dr, dc)
        for dr in range(len(MONSTER))
        for dc in range(len(MONSTER[0]))
        if MONSTER[dr][dc] == "#"
    }
    monsters = 0
    for o in opts(stitched):
        for r in range(len(o) - len(MONSTER) + 1):
            for c in range(len(o[0]) - len(MONSTER[0]) + 1):
                if all(o[r + dr][c + dc] == "#" for dr, dc in checks):
                    monsters += 1
        if monsters:
            break
    rough = [c for l in stitched for c in l].count("#")
    print(rough - monsters * [c for l in MONSTER for c in l].count("#"))


if __name__ == "__main__":
    main()
