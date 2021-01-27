#! /usr/bin/env python3

from utils.intcode import Computer


def main():
    with open("input.txt") as f:
        prog = list(map(int, f.readline().split(",")))
    comp = Computer(prog)
    comp.mem[1] = 12
    comp.mem[2] = 2
    while comp.step():
        pass
    print(comp.mem[0])


if __name__ == "__main__":
    main()
