#! /usr/bin/env python3

from functools import cache
from heapq import heappop, heappush
import networkx as nx


def solve(data: str):
    data = data.splitlines()
    maze = nx.Graph()
    for r, line in enumerate(data):
        for c, ch in enumerate(line):
            if ch != "#":
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
    start = next(n for n, l in maze.nodes.data("label") if l == "@")
    keys = {n: l for n, l in maze.nodes.data("label") if l.islower()}

    hist = set()
    queue = [(0, 0, start, set())]
    while queue:
        _, dist, pos, have = heappop(queue)
        if pos in keys and keys[pos] not in have:
            have = have.copy()
            have.add(keys[pos])
            if len(have) == len(keys):
                return dist
                break
        had = frozenset(have)
        hist.add((pos, had))
        for nbr in neighbors(maze, pos):
            if (nbr, had) not in hist:
                lbl = label(maze, nbr)
                if not lbl.isupper() or lbl.lower() in have:
                    heappush(
                        queue,
                        (
                            dist + heuristic(nbr, have, keys),
                            dist + weight(maze, pos, nbr),
                            nbr,
                            have,
                        ),
                    )


@cache
def neighbors(maze, pos):
    return list(maze.neighbors(pos))


@cache
def label(maze, pos):
    return maze.nodes[pos]["label"]


@cache
def weight(maze, pos, nbr):
    return maze.edges[pos, nbr]["weight"]


def heuristic(pos, have, keys):
    return min(manhattan(pos, k) for k in keys if keys[k] not in have)


@cache
def manhattan(a, b):
    (ar, ac), (br, bc) = a, b
    return abs(ar - br) + abs(ac - bc)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
