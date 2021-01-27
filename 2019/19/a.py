#! /usr/bin/env python3

from utils.intcode import Computer
from itertools import product


def check(prog, x, y):
    io = [y, x]
    comp = Computer(prog, io.pop, io.append)
    while io:
        comp.step()
    while not io:
        comp.step()
    return io.pop()


def main():
    with open("input.txt") as f:
        prog = list(map(int, f.readline().split(",")))
    count = 0
    for x, y in product(range(50), repeat=2):
        count += check(prog, x, y)
    print(count)


if __name__ == "__main__":
    main()
