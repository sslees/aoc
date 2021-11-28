#! /usr/bin/env python3

from itertools import permutations
from utils.intcode import Computer


def solve(data: str):
    prog = list(map(int, data.split(",")))
    signals = []
    for phases in permutations(range(5, 10)):
        comps = {}
        io = [0]
        while not comps or comps[5].running:
            for p in phases:
                if p not in comps:
                    comps[p] = Computer(prog, io.pop, io.append)
                    io.append(p)
                comp = comps[p]
                while comp.running and io:
                    comp.step()
                while not io:
                    comp.step()
        signals.append(io.pop())
    return max(signals)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
