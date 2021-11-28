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


def solve(data: str):
    prog = list(map(int, data.split(",")))
    x, y = 99, 0
    while True:
        while not check(prog, x, y):
            y += 1
        if check(prog, x - 99, y + 99):
            break
        x += 1 if check(prog, x, y + 99) else 100
    return (x - 99) * 10_000 + y


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
