#! /usr/bin/env python3

from collections import defaultdict

import aocd
import networkx as nx

from utils.cells import VNEUMANN


def nbrs(pos):
    return [tuple(map(sum, zip(pos, d))) for d in VNEUMANN]


def solve(data: str):
    heights = defaultdict(lambda: ord("z") + 2)
    for r, row in enumerate(data.splitlines()):
        for c, col in enumerate(row):
            if col == "S":
                start = r, c
                heights[start] = ord("a")
            elif col == "E":
                end = r, c
                heights[end] = ord("z")
            else:
                heights[r, c] = ord(col)
    dg = nx.DiGraph()
    for pos in list(heights):
        for nbr in nbrs(pos):
            if heights[nbr] - heights[pos] <= 1:
                dg.add_edge(pos, nbr)
    return nx.shortest_path_length(dg, start, end)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    aocd.submit(answer, part="a", day=12, year=2022)
