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
    count = 0
    x = y1 = y2 = 0
    while x < 50:
        while not check(prog, x, y1):
            y1 += 1
            if y1 - y2 > 8:
                y1 = y2
                x += 1
        y2 = max(y1, y2)
        while check(prog, x, y2):
            y2 += 1
        if y1 > 49:
            break
        count += min(y2, 50) - y1
        x += 1
    print(count)


if __name__ == "__main__":
    main()
