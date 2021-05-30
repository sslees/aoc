#! /usr/bin/env python3

import random
import re
from collections import deque
from utils.intcode import Computer


class Droid:
    AVOID = [
        "escape pod",
        "giant electromagnet",
        "infinite loop",
        "molten lava",
        "photons",
    ]

    def __init__(self):
        self.output = []
        self.input = deque()
        self.room = None
        self.items = None
        self.alert = None
        self.inv = []
        self.state = "collect"

    def write(self, x):
        self.output.append(chr(x))

    def read(self):
        if not self.input:
            message = "".join(self.output)
            self.output.clear()
            if self.state == "collect":
                # print("C" * 40)
                if matches := re.findall(r"== (.+) ==", message):
                    self.room = matches[-1]
                if matches := re.findall(r"lead:((\n-.+)+)", message):
                    self.doors = matches[-1][0].replace("- ", "").strip().splitlines()
                if matches := re.findall(r"here:((\n-.+)+)", message):
                    self.items = matches[-1][0].replace("- ", "").strip().splitlines()
                    self.items = [e for e in self.items if e not in Droid.AVOID]
                # print(self.room, self.doors, self.items, end=" ")
                if self.items:
                    self.inv.append(self.items.pop())
                    cmd = "take " + self.inv[-1]
                elif self.room == "Security Checkpoint" and len(self.inv) == 8:
                    self.state = "analyze"
                    return self.read()
                else:
                    cmd = random.choice(self.doors)
            elif self.state == "analyze":
                # print("A" * 40)
                if matches := re.findall(r"Alert.+(lighter|heavier)", message):
                    self.alert = matches[-1]
                if matches := re.findall(r"lead:((\n-.+)+)", message):
                    self.doors = matches[-1][0].replace("- ", "").strip().splitlines()
                if matches := re.findall(r"here:((\n-.+)+)", message):
                    self.items = matches[-1][0].replace("- ", "").strip().splitlines()
                # print(self.alert, self.items, end=" ")
                if self.alert == "lighter":
                    cmd = "drop " + self.inv.pop(random.randrange(len(self.inv)))
                    self.alert = None
                elif self.alert == "heavier":
                    self.inv.append(self.items.pop(random.randrange(len(self.items))))
                    cmd = "take " + self.inv[-1]
                    self.alert = None
                else:
                    cmd = random.choice(self.doors)
            # print("Command? " + cmd)
            # print(message, end="")
            self.input.extend(cmd + "\n")
        return ord(self.input.popleft())


def main():
    with open("input.txt") as f:
        prog = list(map(int, f.readline().split(",")))
    droid = Droid()
    comp = Computer(prog, droid.read, droid.write)
    while comp.step():
        pass
    # print("".join(droid.output))
    print(re.search(r"typing (\d+)", "".join(droid.output)).group(1))


if __name__ == "__main__":
    main()
