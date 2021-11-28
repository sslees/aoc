#! /usr/bin/env python3

from collections import deque
from utils.intcode import Computer

SCRIPT = [
    "NOT A J",
    "NOT B T",
    "AND D T",
    "OR T J",
    "NOT C T",
    "AND D T",
    "OR T J",
    "WALK",
]


class Droid:
    def __init__(self):
        self.input = deque("\n".join(SCRIPT) + "\n")
        self.output = []

    def read(self):
        return ord(self.input.popleft())


def solve(data: str):
    prog = list(map(int, data.split(",")))
    droid = Droid()
    comp = Computer(prog, droid.read, droid.output.append)
    while comp.step():
        pass
    return droid.output[-1]


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
