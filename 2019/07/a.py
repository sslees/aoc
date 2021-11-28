#! /usr/bin/env python3

from itertools import permutations
from utils.intcode import Computer


def solve(data: str):
    prog = list(map(int, data.split(",")))
    signals = []
    for phases in permutations(range(5)):
        io = [0]
        for p in phases:
            io.append(p)
            comp = Computer(prog, io.pop, io.append)
            while comp.step():
                pass
        signals.append(io.pop())
    return max(signals)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
