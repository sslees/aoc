#! /usr/bin/env python3

from utils.intcode import Computer


def main():
    with open("input.txt") as f:
        prog = list(map(int, f.readline().split(",")))
    io = []
    comp = Computer(prog, None, io.append)
    while comp.step():
        pass
    data = "".join(map(chr, io)).strip().splitlines()
    parameters = []
    for r in range(1, len(data) - 1):
        for c in range(1, len(data[0]) - 1):
            if all(
                data[r + i][c + j] == "#"
                for i, j, in [(-1, 0), (0, -1), (0, 0), (0, 1), (1, 0)]
            ):
                parameters.append(r * c)
    print(sum(parameters))


if __name__ == "__main__":
    main()
