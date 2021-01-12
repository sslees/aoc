#! /bin/env python3

from functools import cache
import utils.cells as cells


class VisNbr(cells.Automaton):
    @cache
    def neighbors(self, pos):
        nbrs = []
        for d in self.dirs:
            vis = None
            p = pos
            while vis is None:
                p = tuple(map(sum, zip(p, d)))
                if p not in self.cells:
                    break
                vis = self.cells[p]
            nbrs.append(p)
        return nbrs


def main():
    with open("input.txt") as f:
        lines = f.readlines()
    seats = {}
    for r, line in enumerate(lines):
        for c, char in enumerate(line.strip()):
            seats[c, r] = None if char == "." else char == "#"
    auto = VisNbr(seats, infinite=False, rule=cells.RULE((0,), (0, 1, 2, 3, 4)))
    while auto.step():
        pass
    print(auto.population())


if __name__ == "__main__":
    main()
