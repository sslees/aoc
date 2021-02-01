#! /usr/bin/env python3

from collections import defaultdict
from functools import cache
from utils.intcode import Computer
import networkx as nx

N, S, W, E = 1, 2, 3, 4


class Controller:
    def __init__(self):
        self.pos = 0, 0
        self.g = nx.DiGraph()
        self.g.add_node(self.pos, lbl="D")

    @cache
    def neighbors(self, pos):
        c, r = self.pos
        return {N: (c, r - 1), S: (c, r + 1), W: (c - 1, r), E: (c + 1, r)}

    def command(self):
        for cmd, nxt in self.neighbors(self.pos).items():
            if nxt not in self.g:
                self.nxt = nxt
                self.cmd = cmd
                return self.cmd
        if prv := next(self.g.predecessors(self.pos), None):
            self.nxt = prv
            self.cmd = self.g.edges[prv, self.pos]["rev"]
            return self.cmd
        paths = nx.algorithms.shortest_paths.generic.shortest_path(
            self.g.to_undirected(), self.finish
        )
        path = max(paths.values(), key=len)
        print(len(path) - 1)
        # for p in path[1:]:
        #     self.g.nodes[p]["lbl"] = "o"
        # chars = defaultdict(lambda: " ", list(self.g.nodes(data="lbl")))
        # cs, rs = list(zip(*chars))
        # cs, rs = range(min(cs), max(cs) + 1), range(min(rs), max(rs) + 1)
        # print("\n".join("".join(chars[x, y] for x in cs) for y in rs))

    def status(self, code):
        if code == 0:  # wall
            self.g.add_node(self.nxt, lbl="#")
        elif code in (1, 2):  # moved, done
            if self.nxt not in self.g:
                rev = {N: S, S: N, W: E, E: W}[self.cmd]
                if code == 1:  # moved
                    self.g.add_node(self.nxt, lbl=".")
                else:  # done
                    self.g.add_node(self.nxt, lbl="O")
                    self.finish = self.nxt
                self.g.add_edge(self.pos, self.nxt, rev=rev)
            self.pos = self.nxt


def main():
    with open("input.txt") as f:
        prog = list(map(int, f.readline().split(",")))
    ctrl = Controller()
    comp = Computer(prog, ctrl.command, ctrl.status)
    while comp.step():
        pass


if __name__ == "__main__":
    main()
