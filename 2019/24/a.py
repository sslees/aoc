#! /bin/env python3

import utils.cells as cells


def main():
    with open("input.txt") as f:
        lines = [l.strip() for l in f.readlines()]
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
    print(sum(2 ** i for i, ch in enumerate(state.replace("\n", "")) if ch == "#"))


if __name__ == "__main__":
    main()
