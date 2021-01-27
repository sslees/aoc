#! /usr/bin/env python3

from collections import defaultdict, namedtuple
from functools import cache
from itertools import product
from time import sleep
import curses

# neighborhoods
HEX = tuple((dx, dy) for dx, dy in product((-1, 0, 1), repeat=2) if dx != dy)
MOORE = lambda dimension=2: tuple(
    p for p in product((-1, 0, 1), repeat=dimension) if any(p)
)
VNEUMANN = tuple(
    (dx, dy) for dx, dy in product((-1, 0, 1), repeat=2) if bool(dx) ^ bool(dy)
)

# rules (By/Sx format)
RULE = namedtuple("Rule", ("b", "s"))
LIFE = RULE((3,), (2, 3))


class Automaton:
    def __init__(self, configuration, infinite=True, rule=LIFE, neighborhood=MOORE()):
        self.rule = rule
        self.dirs = neighborhood
        self.cells = defaultdict(bool if infinite else type(None), configuration)
        for p in list(self.cells):
            self.cells |= {n: self.cells[n] for n in self.neighbors(p)}
        self.changes = set(self.cells)

    @cache
    def neighbors(self, pos):
        return [tuple(map(sum, zip(pos, d))) for d in self.dirs]

    def evaluate(self, pos):
        cur = self.cells[pos]
        if cur is None:
            return None, False
        ct = [self.cells[n] for n in self.neighbors(pos)].count(True)
        b, s = self.rule
        nxt = ct in s if cur is True else ct in b if cur is False else None
        return nxt, nxt != cur

    def step(self):
        updates = {}
        changes = set()
        for pos in list(self.changes):
            updates[pos], diff = self.evaluate(pos)
            if diff:
                changes.add(pos)
                changes.update(self.neighbors(pos))
        self.cells |= updates
        self.changes = changes
        return bool(changes)

    def population(self):
        return list(self.cells.values()).count(True)

    def __repr__(self):  # TODO
        chars = {
            p: "#" if v else "." if v is False else "?" for p, v in self.cells.items()
        }
        dims = list(zip(*chars))
        if len(dims) >= 2:
            xs, ys = dims[:2]
            return (
                "\n".join(
                    "".join(chars[x, y] for x in range(min(xs) + 1, max(xs)))
                    for y in range(min(ys) + 1, max(ys))
                )
                + "\n"
            )
        # xs, ys = zip(*cells)
        # print(
        #     "\n".join(
        #         " " * (y - min(ys))
        #         + "".join(
        #             ("#" if cells[x, y] else ".") + (" " if x or y else ")")
        #             for x in range(min(xs), max(xs) + 1)
        #         ).rstrip()
        #         for y in range(max(ys), min(ys) - 1, -1)
        #     )
        #     + "\n"
        # )
        #
        # s = len(cube)
        # for z, slc in enumerate(cube):
        #     print("z=", z - s // 2, sep="")
        #     for r in slc:
        #         print("".join(r))
        #     print()
        #
        # half = len(hcube) // 2
        # for w, cube in enumerate(hcube):
        #     for z, slc in enumerate(cube):
        #         print("z={}, w={}".format(z - half, w - half))
        #         for r in slc:
        #             print("".join(r))
        #         print()


def main(stdscr):
    cols, rows = 80, 25
    cfg = {p: False for p in product(range(cols), range(rows))}
    for x, y in (0, 0), (4, 0), (5, 0), (6, 0), (1, 0), (1, 1), (1, 2), (1, 5), (2, 1):
        cfg[x + cols // 2, y + rows // 2] = True
    auto = Automaton(cfg, False)
    curses.curs_set(0)
    stdscr.clear()
    print(auto)
    while auto.step():
        stdscr.addstr(0, 0, str(auto))
        sleep(0.1)
        stdscr.refresh()
    stdscr.getch()


if __name__ == "__main__":
    curses.wrapper(main)
