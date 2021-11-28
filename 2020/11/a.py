#! /bin/env python3

import utils.cells as cells


def solve(data: str):
    lines = data.splitlines()
    seats = {}
    for r, line in enumerate(lines):
        for c, char in enumerate(line):
            seats[c, r] = None if char == "." else char == "#"
    auto = cells.Automaton(seats, infinite=False, rule=([0], [0, 1, 2, 3]))
    while auto.step():
        pass
    return auto.population()


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
