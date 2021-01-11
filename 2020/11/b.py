#! /bin/env python3

import utils.cells as cells


class VisNbr(cells.Automaton):
    def evaluate(self, pos):
        cur = self.cells[pos]
        if cur is None:
            return None, False
        ct = 0
        for dx, dy in self.dirs:
            vis = None
            x, y = pos
            while vis is None:
                y += dy
                x += dx
                if (x, y) not in self.cells:
                    break
                vis = self.cells[x, y]
            ct += bool(vis)
        b, s = self.rule
        nxt = ct in s if cur is True else ct in b if cur is False else None
        return nxt, nxt != cur


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
