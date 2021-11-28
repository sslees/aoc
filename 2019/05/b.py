#! /usr/bin/env python3

from utils.intcode import Computer


def solve(data: str):
    prog = list(map(int, data.split(",")))
    io = [5]
    comp = Computer(prog, io.pop, io.append)
    while comp.step():
        pass
    return io.pop()


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
