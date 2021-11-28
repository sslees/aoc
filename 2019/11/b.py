#! /usr/bin/env python3

from collections import defaultdict
from utils.intcode import Computer
import utils.ocr as ocr


class Robot:
    def __init__(self):
        self.panels = defaultdict(int)
        self.x = 0
        self.y = 0
        self.dir = 90

    def camera(self):
        return self.panels[self.x, self.y]

    def paint(self, val):
        self.panels[self.x, self.y] = val

    def turn(self, val):
        self.dir = (self.dir - 90 if val else self.dir + 90) % 360
        self.x += 1 if self.dir == 0 else -1 if self.dir == 180 else 0
        self.y += 1 if self.dir == 90 else -1 if self.dir == 270 else 0


def solve(data: str):
    prog = list(map(int, data.split(",")))
    robo = Robot()
    robo.panels[0, 0] = 1
    io = []
    comp = Computer(prog, robo.camera, io.append)
    while comp.running:
        while comp.running and not io:
            comp.step()
        if not comp.running:
            break
        robo.paint(io.pop())
        while not io:
            comp.step()
        robo.turn(io.pop())
    return ocr.scan(robo.panels)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
