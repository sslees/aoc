#! /usr/bin/env python3

from functools import cache
from utils.intcode import Computer
import networkx as nx

N, S, W, E = 1, 2, 3, 4


class Controller:
    def __init__(self):
        self.pos = 0, 0
        self.g = nx.DiGraph()

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
        lens = nx.algorithms.shortest_paths.generic.shortest_path_length(
            self.g.to_undirected(), self.finish
        )
        print(max(lens.values()))

    def status(self, code):
        if code == 0:  # wall
            self.g.add_node(self.nxt)
        elif code in (1, 2):  # moved, done
            if self.nxt not in self.g:
                rev = {N: S, S: N, W: E, E: W}[self.cmd]
                self.g.add_edge(self.pos, self.nxt, rev=rev)
                if code == 2:  # done
                    self.finish = self.nxt
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
