#! /usr/bin/env python3

from utils.intcode import Computer


def main():
    with open("input.txt") as f:
        prog = list(map(int, f.readline().split(",")))
    io = [1]
    comp = Computer(prog, io.pop, io.append)
    while comp.step():
        pass
    print(io.pop())


if __name__ == "__main__":
    main()
