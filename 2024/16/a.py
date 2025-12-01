#! /usr/bin/env python3

import math
import random
import re
import statistics
from collections import Counter, defaultdict, deque, namedtuple
from functools import cache
from itertools import (
    combinations,
    count,
    cycle,
    pairwise,
    permutations,
    product,
    repeat,
)

import aocd
import networkx as nx
from parse import parse
from utils.grid import defaultgrid, dimensions


def solve(data: str):
    data = data.splitlines()
    maze = nx.Graph()
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            if c != "#":
                maze.add_node((x, y), label=c)
                if (x - 1, y) in maze:
                    maze.add_edge((x, y), (x - 1, y), weight=1, dir="h")
                if (x, y - 1) in maze:
                    maze.add_edge((x, y), (x, y - 1), weight=1, dir="v")
    start = next(p for p, c in maze.nodes.data("label") if c == "S")
    end = next(p for p, c in maze.nodes.data("label") if c == "E")
    adds = []
    removes = []
    for node in maze.nodes:
        if len(list(maze.neighbors(node))) > 2:
            for n1, n2 in combinations(maze.neighbors(node), r=2):
                if maze.edges[node, n1]["dir"] == maze.edges[node, n2]["dir"]:
                    adds.append((n1, n2, {"weight": 2}))
                else:
                    adds.append((n1, n2, {"weight": 1002}))
                removes.append(node)
    maze.add_edges_from(adds)
    maze.remove_nodes_from(removes)
    return nx.shortest_path_length(maze, start, end)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    # aocd.submit(answer, part="a", day=16, year=2024)
