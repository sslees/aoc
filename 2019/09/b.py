#! /usr/bin/env python3

from utils.intcode import Computer


def solve(data: str):
    io = [2]
    prog = list(map(int, data.split(",")))
    comp = Computer(prog, io.pop, io.append)
    while comp.step():
        pass
    return io[0]


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
