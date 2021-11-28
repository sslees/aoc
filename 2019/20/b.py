#! /bin/env python3

from itertools import count, product
import networkx as nx
import re


def solve(data: str):
    data = data.splitlines()
    base = nx.Graph()
    for r, line in enumerate(data):
        for c, ch in enumerate(line):
            if ch == ".":
                base.add_node((r, c))
                for nbr in [(r - 1, c), (r, c - 1)]:
                    if nbr in base:
                        base.add_edge((r, c), nbr, weight=1)
    for n, deg in list(base.degree):
        if deg == 2:
            u, v = base.neighbors(n)
            wt = base.edges[u, n]["weight"] + base.edges[n, v]["weight"]
            base.add_edge(u, v, weight=wt)
            base.remove_node(n)
    inner = {}
    outer = {}
    for r, line in enumerate(data):
        for m in re.finditer(r" (\w\w)\.", line):
            inner[m[1]] = (r, m.end() - 1)
        for m in re.finditer(r"\.(\w\w) ", line):
            inner[m[1]] = (r, m.start())
        for m in re.finditer(r"^(\w\w)\.", line):
            outer[m[1]] = (r, m.end() - 1)
        for m in re.finditer(r"\.(\w\w)$", line):
            outer[m[1]] = (r, m.start())
    for c, line in enumerate(map("".join, zip(*data))):
        for m in re.finditer(r" (\w\w)\.", line):
            inner[m[1]] = (m.end() - 1, c)
        for m in re.finditer(r"\.(\w\w) ", line):
            inner[m[1]] = (m.start(), c)
        for m in re.finditer(r"^(\w\w)\.", line):
            outer[m[1]] = (m.end() - 1, c)
        for m in re.finditer(r"\.(\w\w)$", line):
            outer[m[1]] = (m.start(), c)
    maze = nx.Graph()
    portals = set(inner) & set(outer)
    for depth in count():
        for u, v, wt in base.edges.data("weight"):
            maze.add_edge((depth, u), (depth, v), weight=wt)
        if depth:
            for lbl in portals:
                maze.add_edge((depth - 1, inner[lbl]), (depth, outer[lbl]), weight=1)
        try:
            edge = (0, outer["AA"]), (0, outer["ZZ"])
            len = nx.shortest_path_length(maze, *edge, "weight")
            return len
            break
        except:
            pass


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
