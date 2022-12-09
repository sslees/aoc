#! /usr/bin/env python3

import re
from collections import defaultdict

import networkx as nx


def solve(data: str):
    data = data.splitlines()
    w = max(len(l) for l in data)
    data = [l.ljust(w) for l in data]
    maze = nx.Graph()
    for r, line in enumerate(data):
        for c, ch in enumerate(line):
            if ch == ".":
                maze.add_node((r, c))
                for nbr in [(r - 1, c), (r, c - 1)]:
                    if nbr in maze:
                        maze.add_edge((r, c), nbr, weight=1)
    for n, deg in list(maze.degree):
        if deg == 2:
            u, v = maze.neighbors(n)
            wt = maze.edges[u, n]["weight"] + maze.edges[n, v]["weight"]
            maze.add_edge(u, v, weight=wt)
            maze.remove_node(n)
    portals = defaultdict(list)
    for r, line in enumerate(data):
        for m in re.finditer(r"(\w\w)\.", line):
            portals[m[1]].append((r, m.end() - 1))
        for m in re.finditer(r"\.(\w\w)", line):
            portals[m[1]].append((r, m.start()))
    for c, line in enumerate(map("".join, zip(*data))):
        for m in re.finditer(r"(\w\w)\.", line):
            portals[m[1]].append((m.end() - 1, c))
        for m in re.finditer(r"\.(\w\w)", line):
            portals[m[1]].append((m.start(), c))
    for tiles in portals.values():
        if len(tiles) == 2:
            maze.add_edge(*tiles, weight=1)
    return nx.shortest_path_length(maze, portals["AA"][0], portals["ZZ"][0], "weight")


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
