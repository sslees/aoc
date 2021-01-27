#! /usr/bin/env python3

from utils.intcode import Computer


def main():
    with open("input.txt") as f:
        prog = list(map(int, f.readline().split(",")))
    bricks = set()
    io = []
    comp = Computer(prog, None, io.append)
    while comp.running:
        while len(io) < 3 and comp.running:
            comp.step()
        if not comp.running:
            break
        val, y, x = io.pop(), io.pop(), io.pop()
        if val == 2:
            bricks.add((x, y))
    print(len(bricks))


if __name__ == "__main__":
    main()
