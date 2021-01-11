#! /bin/env python3

import utils.cells as cells


def main():
    with open("input.txt") as f:
        lines = f.readlines()
    seats = {}
    for r, line in enumerate(lines):
        for c, char in enumerate(line.strip()):
            seats[c, r] = None if char == "." else char == "#"
    auto = cells.Automaton(seats, infinite=False, rule=cells.RULE((0,), (0, 1, 2, 3)))
    while auto.step():
        pass
    print(auto.population())


if __name__ == "__main__":
    main()
