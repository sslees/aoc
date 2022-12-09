#! /usr/bin/env python3

import utils.cells as cells


def solve(data: str):
    lines = data.splitlines()
    bugs = {}
    for r, line in enumerate(lines):
        for c, char in enumerate(line):
            bugs[c, r] = char == "#"
    auto = cells.Automaton(
        bugs, infinite=False, neighborhood=cells.VNEUMANN, rule=([1, 2], [1])
    )
    states = set()
    while True:
        auto.step()
        state = str(auto)
        if state in states:
            break
        states.add(state)
    return sum(2**i for i, ch in enumerate(state.replace("\n", "")) if ch == "#")


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
