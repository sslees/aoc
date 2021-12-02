#! /usr/bin/env python3

import utils.cells as cells


def solve(data: str):
    lines = data.splitlines()
    config = {}
    for r, line in enumerate(lines):
        for c, char in enumerate(line):
            config[c, r, 0] = char == "#"
    auto = cells.Automaton(config, neighborhood=cells.MOORE(3))
    for _ in range(6):
        auto.step()
    return auto.population()


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
