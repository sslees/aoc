#! /usr/bin/env python3

from utils.intcode import Computer


def solve(data: str):
    prog = list(map(int, data.split(",")))
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
    return sum(parameters)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
