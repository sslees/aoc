#! /usr/bin/env python3

from collections import deque
from utils.intcode import Computer
import random
import re

AVOID = "escape pod", "giant electromagnet", "infinite loop", "molten lava", "photons"
REV = {"north": "south", "east": "west", "south": "north", "west": "east", None: None}


class Droid:
    def __init__(self):
        self.input = deque()
        self.output = []
        self.explored = False
        self.hist = {}
        self.exit = None
        self.inv = []
        self.items = deque()

    def message(self):
        msg = "".join(map(chr, self.output))
        self.output.clear()
        return msg

    def explore(self, msg):
        if room := re.findall(r"== (.+) ==", msg):
            self.room = room[-1]
        if doors := re.findall(r"lead:((\n-.+)+)", msg):
            self.doors = doors[-1][0].replace("- ", "").strip().splitlines()
        if item := re.search(r"here:\n- (.+)", msg):
            item = item[1]
        if self.room not in self.hist:
            self.hist[self.room] = [self.exit]
        hist = self.hist[self.room]
        if item and item not in AVOID:
            self.inv.append(item)
            return "take " + self.inv[-1]
        elif len(self.inv) == 8 and self.room == "Security Checkpoint":
            self.explored = next((d for d in self.doors if d != hist[0]))
        else:
            dir = next((d for d in self.doors if d not in hist), hist[0])
            self.exit = REV[dir]
            if not dir:
                self.hist = {}
                return self.explore(msg)
            if dir not in hist:
                hist.append(dir)
            return dir

    def analyze(self, msg):
        if "lighter" in msg:
            self.items.append(self.inv.pop(random.randrange(len(self.inv))))
            return "drop " + self.items[-1]
        if "heavier" in msg:
            self.inv.append(self.items.popleft())
            return "take " + self.inv[-1]
        return self.explored

    def read(self):
        if not self.input:
            msg = self.message()
            if not self.explored:
                cmd = self.explore(msg)
            if self.explored:
                cmd = self.analyze(msg)
            self.input.extend(cmd + "\n")
        return ord(self.input.popleft())


def solve(data: str):
    prog = list(map(int, data.split(",")))
    droid = Droid()
    comp = Computer(prog, droid.read, droid.output.append)
    while comp.step():
        pass
    return re.search(r"typing (\d+)", droid.message())[1]


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
