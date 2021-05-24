#! /usr/bin/env python3

from utils.intcode import Computer


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
    x, y = 99, 0
    while True:
        while not check(prog, x, y):
            y += 1
        if check(prog, x - 99, y + 99):
            break
        x += 1 if check(prog, x, y + 99) else 100
    print((x - 99) * 10_000 + y)


if __name__ == "__main__":
    main()
