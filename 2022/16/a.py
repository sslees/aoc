#! /usr/bin/env python3

import math
import random
import re
import statistics
from collections import Counter, defaultdict, deque, namedtuple
from functools import cache
from heapq import heappop, heappush
from itertools import combinations, count, cycle, permutations, product, repeat

import aocd
import networkx as nx
from parse import parse

TIME = 30


@cache
def neighbors(maze: nx.Graph, pos):
    return list(maze.neighbors(pos))


@cache
def path(maze, a, b):
    return nx.shortest_path_length(maze, a, b)


def solve(data: str):
    rates = {}
    maze = nx.Graph()
    for l in data.splitlines():
        try:
            left, right = l.split("; tunnels lead to valves ")
        except ValueError:
            left, right = l.split("; tunnel leads to valve ")
        valve, rate = parse("Valve {} has flow rate={:d}", left)
        tunnels = right.split(", ")
        rates[valve] = rate
        maze.add_node(valve)
        for dest in tunnels:
            maze.add_edge(valve, dest, weight=1)
    # max_rate = sum(rates.values())
    hist = set()
    queue = [(None, 0, 0, 0, "AA", set())]
    while queue:
        _, time, released, rate, pos, open = heappop(queue)
        released = -released
        if time == TIME:
            return released
        opened = frozenset(open)
        hist.add((pos, opened))
        if not pos in open:
            heappush(
                queue,
                (
                    -(
                        released
                        + rate * (TIME - time)
                        + sum(
                            r * (TIME - time - path(maze, pos, v) - 1)
                            for v, r in rates.items()
                            if v not in opened
                        )
                    ),
                    time + 1,
                    -(released + rate),
                    rate + rates[pos],
                    pos,
                    open | {pos},
                ),
            )
        for nbr in neighbors(maze, pos):
            if (nbr, opened) not in hist:
                heappush(
                    queue,
                    (
                        -(
                            released
                            + rate * (TIME - time)
                            + sum(
                                r
                                * (
                                    TIME
                                    - time
                                    - nx.shortest_path_length(maze, nbr, v)
                                    - 1
                                )
                                for v, r in rates.items()
                                if v not in opened
                            )
                        ),
                        time + 1,
                        -(released + rate),
                        rate,
                        nbr,
                        open,
                    ),
                )
    return None


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    aocd.submit(answer, part="a", day=16, year=2022)
