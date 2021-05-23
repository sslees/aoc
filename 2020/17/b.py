#! /bin/env python3

import utils.cells as cells


def main():
    with open("input.txt") as f:
        lines = [l.strip() for l in f.readlines()]
    config = {}
    for r, line in enumerate(lines):
        for c, char in enumerate(line):
            config[c, r, 0, 0] = char == "#"
    auto = cells.Automaton(config, neighborhood=cells.MOORE(4))
    for _ in range(6):
        auto.step()
    print(auto.population())


if __name__ == "__main__":
    main()
