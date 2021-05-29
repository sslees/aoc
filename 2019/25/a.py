#! /usr/bin/env python3

import random
from collections import deque
from utils.intcode import Computer


class Droid:
    OPTS = {
        "n": "north",
        "s": "south",
        "e": "east",
        "w": "west",
        "t": "take",
        "d": "drop",
        "i": "inv",
    }

    def __init__(self):
        self.io = deque()

    def read(self):
        if not self.io:
            while (cmd := input(f"> ({'/'.join(Droid.OPTS)}?) ")) not in Droid.OPTS:
                pass
            # cmd = random.choice("nsew")
            print(cmd)
            self.io.extend(Droid.OPTS[cmd] + "\n")
        return ord(self.io.popleft())

    def write(self, x):
        print(chr(x), end="")


def main():
    with open("input.txt") as f:
        prog = list(map(int, f.readline().split(",")))
    droid = Droid()
    comp = Computer(prog, droid.read, droid.write)
    while comp.step():
        pass


if __name__ == "__main__":
    main()
