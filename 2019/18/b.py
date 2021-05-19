#! /bin/env python3

from functools import cache
from heapq import heappop, heappush
import networkx as nx


def main(filename):
    with open(filename) as f:
        data = [l.strip() for l in f.readlines()]
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
    # doors = {n: l for n, l in maze.nodes.data("label") if l.isupper()}
    # vaults = [
    #     {doors[n].lower() for n in nx.node_connected_component(maze, pos) if n in doors}
    #     for pos in robots
    # ]

    hist = set()
    queue = [(0, 0, robots, set())]
    while queue:
        _, dist, robots, have = heappop(queue)
        # print("trying", dist, robots, have)
        for vault, pos in enumerate(robots):
            if pos in keys and keys[pos] not in have:
                # print("found", keys[pos])
                have = have.copy()
                have.add(keys[pos])
                if len(have) == len(keys):
                    print(dist)
                    return
        had = frozenset(have)
        for vault, pos in enumerate(robots):
            hist.add((pos, had))
            # print("visited", pos, list(sorted(had)))
        for vault, pos in enumerate(robots):
            # had = frozenset(have)
            for nbr in neighbors(maze, pos):
                if (nbr, had) not in hist:
                    lbl = label(maze, nbr)
                    if not lbl.isupper() or lbl.lower() in have:
                        rbs = robots.copy()
                        rbs[vault] = nbr
                        heappush(
                            queue,
                            (
                                dist + heuristic(nbr, have, keys),
                                dist + weight(maze, pos, nbr),
                                rbs,
                                have,
                            ),
                        )
                        # print("enq", dist + weight(maze, pos, nbr), rbs, have)
                    # else:
                    # print("locked", nbr, list(sorted(had)))
                # else:
                # print("ignoring", nbr, list(sorted(had)))
        # print("--------")


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
    # return 0


@cache
def manhattan(a, b):
    (ar, ac), (br, bc) = a, b
    return abs(ar - br) + abs(ac - bc)


if __name__ == "__main__":
    # main("e6b.txt")  # 8
    # main("e7b.txt")  # 24
    # main("e8b.txt")  # 32
    # main("e9b.txt")  # 72
    main("inputB.txt")  # 1640
