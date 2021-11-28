#! /usr/bin/env python3

from utils.intcode import Computer


def solve(data: str):
    prog = list(map(int, data.split(",")))
    io = []
    comp = Computer(prog, None, io.append)
    bricks = 0
    while comp.running:
        while len(io) < 3 and comp.running:
            comp.step()
        if not comp.running:
            break
        val, _, _ = io.pop(), io.pop(), io.pop()
        bricks += val == 2
    return bricks


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
