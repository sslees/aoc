#! /bin/env python3

from functools import cache
import utils.cells as cells


class RecursiveAuto(cells.Automaton):
    @cache
    def neighbors(self, cell):
        cx, cy, d = cell
        nbrs = []
        for nx, ny in super().neighbors((cx, cy)):
            if nx == ny == 2:
                if cx == 1:
                    nbrs.extend((0, y, d + 1) for y in range(5))
                elif cx == 3:
                    nbrs.extend((4, y, d + 1) for y in range(5))
                elif cy == 1:
                    nbrs.extend((x, 0, d + 1) for x in range(5))
                else:  # cy == 3
                    nbrs.extend((x, 4, d + 1) for x in range(5))
            elif nx == -1:
                nbrs.append((1, 2, d - 1))
            elif nx == 5:
                nbrs.append((3, 2, d - 1))
            elif ny == -1:
                nbrs.append((2, 1, d - 1))
            elif ny == 5:
                nbrs.append((2, 3, d - 1))
            else:
                nbrs.append((nx, ny, d))
        return nbrs


def main():
    with open("input.txt") as f:
        lines = [l.strip() for l in f.readlines()]
    bugs = {}
    for r, line in enumerate(lines):
        for c, char in enumerate(line):
            bugs[c, r, 0] = char == "#"
    del bugs[2, 2, 0]
    auto = RecursiveAuto(bugs, neighborhood=cells.VNEUMANN, rule=([1, 2], [1]))
    for _ in range(200):
        auto.step()
    print(auto.population())


if __name__ == "__main__":
    main()
