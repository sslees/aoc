#! /usr/bin/env python3

from utils.intcode import Computer


def main():
    with open("input.txt") as f:
        prog = list(map(int, f.readline().split(",")))
    comp = Computer(prog, [1].pop, print)
    while comp.step():
        pass


if __name__ == "__main__":
    main()
