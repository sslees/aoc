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

DELTAS = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}


def add(p, d):
    return p[0] + d[0], p[1] + d[1]


def pretty(grid, width, height):
    for y in range(height):
        for x in range(width):
            print(grid[x, y], end="")
        print()
    print()


def solve(data: str):
    warehouse, moves = data.split("\n\n")
    grid = defaultgrid(warehouse)
    width, height = dimensions(warehouse)
    moves = moves.replace("\n", "")
    robot = next(p for p, c in grid.items() if c == "@")
    # print(width, height, robot)
    # print(moves)
    # print("initial state")
    # pretty(grid, width, height)
    for m in moves:
        # print("move", m)
        delta = DELTAS[m]
        oppo = -delta[0], -delta[1]
        target = add(robot, delta)
        boxes = 0
        while True:
            if grid[target] == "#":
                # print("hit wall")
                break
            elif grid[target] == "O":
                boxes += 1
                # print("boxes:", boxes)
            elif grid[target] == ".":
                for _ in range(boxes + 1):
                    grid[target] = grid[add(target, oppo)]
                    target = add(target, oppo)
                grid[target] = "."
                robot = add(target, delta)
                break
            else:
                # print("UNKNOWN TARGET")
                break
            target = add(target, delta)
        # pretty(grid, width, height)
    score = 0
    for (x, y), c in grid.items():
        if c == "O":
            score += 100 * y + x
    return score


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    #     data = """########
    # #..O.O.#
    # ##@.O..#
    # #...O..#
    # #.#.O..#
    # #...O..#
    # #......#
    # ########

    # <^^>>>vv<v>>v<<"""
    answer = solve(data)
    print(answer)
    # aocd.submit(answer, part="a", day=15, year=2024)
