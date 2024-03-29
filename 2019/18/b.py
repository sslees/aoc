#! /usr/bin/env python3

from functools import cache
from heapq import heappop, heappush

import networkx as nx


def solve(data: str):
    data = data.splitlines()
    r, c = len(data) // 2, len(data[0]) // 2
    data[r - 1] = data[r - 1][: c - 1] + "@#@" + data[r - 1][c + 2 :]
    data[r] = data[r][: c - 1] + "###" + data[r][c + 2 :]
    data[r + 1] = data[r + 1][: c - 1] + "@#@" + data[r + 1][c + 2 :]

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
    robots = [n for n, l in maze.nodes.data("label") if l == "@"]
    keys = {n: l for n, l in maze.nodes.data("label") if l.islower()}
    vaults = [nx.node_connected_component(maze, robot) & set(keys) for robot in robots]

    hist = set()
    queue = [(0, 0, robots, set())]
    while queue:
        _, dist, robots, have = heappop(queue)
        for vault, pos in enumerate(robots):
            if pos in keys and keys[pos] not in have:
                have = have.copy()
                have.add(keys[pos])
                if len(have) == len(keys):
                    return dist
                    return
        had = frozenset(have)
        for vault, pos in enumerate(robots):
            hist.add((pos, had))
        for vault, pos in enumerate(robots):
            opts = [k for k in vaults[vault] if keys[k] not in have]
            if opts:
                for nbr in neighbors(maze, pos):
                    if (nbr, had) not in hist:
                        lbl = label(maze, nbr)
                        if not lbl.isupper() or lbl.lower() in have:
                            rbs = robots.copy()
                            rbs[vault] = nbr
                            heappush(
                                queue,
                                (
                                    dist + heuristic(nbr, opts),
                                    dist + weight(maze, pos, nbr),
                                    rbs,
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


def heuristic(pos, opts):
    return min(manhattan(pos, k) for k in opts)


@cache
def manhattan(a, b):
    (ar, ac), (br, bc) = a, b
    return abs(ar - br) + abs(ac - bc)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
