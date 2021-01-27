#! /usr/bin/env python3

from itertools import permutations
from utils.intcode import Computer


def main():
    with open("input.txt") as f:
        prog = list(map(int, f.readline().split(",")))
    signals = []
    for phases in permutations(range(5)):
        io = [0]
        for p in phases:
            io.append(p)
            comp = Computer(prog, io.pop, io.append)
            while comp.step():
                pass
        signals.append(io.pop())
    print(max(signals))


if __name__ == "__main__":
    main()
