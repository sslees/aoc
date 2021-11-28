#! /bin/env python3

from functools import cache
import utils.cells as cells


class VisNbrAuto(cells.Automaton):
    @cache
    def neighbors(self, cell):
        nbrs = []
        for dir in self.dirs:
            vis = None
            pos = cell
            while vis is None:
                pos = tuple(map(sum, zip(pos, dir)))
                if pos not in self.cells:
                    break
                vis = self.cells[pos]
            nbrs.append(pos)
        return nbrs


def solve(data: str):
    lines = data.splitlines()
    seats = {}
    for r, line in enumerate(lines):
        for c, char in enumerate(line):
            seats[c, r] = None if char == "." else char == "#"
    auto = VisNbrAuto(seats, infinite=False, rule=([0], [0, 1, 2, 3, 4]))
    while auto.step():
        pass
    return auto.population()


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
