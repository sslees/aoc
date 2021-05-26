#! /usr/bin/env python3

from utils.intcode import Computer


def main():
    with open("input.txt") as f:
        prog = list(map(int, f.readline().split(",")))
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
    print(bricks)


if __name__ == "__main__":
    main()
