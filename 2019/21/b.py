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
    "RUN",
]


class Droid:
    def __init__(self):
        self.input = deque()
        self.output = []

    def message(self):
        msg = "".join(map(chr, self.output))
        self.output.clear()
        return msg

    def read(self):
        if not self.input:
            msg = self.message()
            print(msg)
            cmd = "\n".join(SCRIPT) + "\n"
            print(cmd)
            self.input.extend(cmd + "\n")
        return ord(self.input.popleft())


def main():
    with open("input.txt") as f:
        prog = list(map(int, f.readline().split(",")))
    droid = Droid()
    comp = Computer(prog, droid.read, droid.output.append)
    while comp.step():
        pass
    print(droid.message())


if __name__ == "__main__":
    main()
