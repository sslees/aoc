#! /bin/env python3

from collections import defaultdict
import networkx as nx
import re


def main():
    with open("input.txt") as f:
        data = [l[:-1] for l in f.readlines()]
    maze = nx.Graph()
    for r, line in enumerate(data):
        for c, ch in enumerate(line):
            if ch == ".":
                maze.add_node((r, c), label=ch)
                for nbr in [(r - 1, c), (r, c - 1)]:
                    if nbr in maze:
                        maze.add_edge((r, c), nbr, weight=1)
    for n, deg in list(maze.degree):
        if deg == 2 and maze.nodes[n]["label"] == ".":
            u, v = maze.neighbors(n)
            wt = maze.edges[u, n]["weight"] + maze.edges[n, v]["weight"]
            maze.add_edge(u, v, weight=wt)
            maze.remove_node(n)
    lbls = defaultdict(list)
    for r, line in enumerate(data):
        for m in re.finditer(r"(\w\w)\.", line):
            lbls[m[1]].append((r, m.end() - 1))
        for m in re.finditer(r"\.(\w\w)", line):
            lbls[m[1]].append((r, m.start()))
    for c, line in enumerate(map("".join, zip(*data))):
        for m in re.finditer(r"(\w\w)\.", line):
            lbls[m[1]].append((m.end() - 1, c))
        for m in re.finditer(r"\.(\w\w)", line):
            lbls[m[1]].append((m.start(), c))
    for lbl in lbls.values():
        if len(lbl) == 2:
            maze.add_edge(*lbl, weight=1)
    print(nx.shortest_path_length(maze, lbls["AA"][0], lbls["ZZ"][0], "weight"))


if __name__ == "__main__":
    main()
