#! /usr/bin/env python3

from utils.intcode import Computer


def solve(data: str):
    prog = list(map(int, data.split(",")))
    comp = Computer(prog)
    comp.mem[1] = 12
    comp.mem[2] = 2
    while comp.step():
        pass
    return comp.mem[0]


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
