from collections import defaultdict, namedtuple
from functools import cache
from itertools import product

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
        xs, ys = zip(*self.cells)
        return (
            "\n".join(
                "".join(
                    "#"
                    if self.cells[x, y]
                    else "L"
                    if self.cells[x, y] is False
                    else "."
                    for x in range(min(xs) + 1, max(xs))
                )
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
