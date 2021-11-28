#! /usr/bin/env python3

from itertools import combinations
from utils.intcode import Computer


class Robot:
    FRONT = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def __init__(self, maze):
        self.actions = []
        self.maze = maze
        self.maxr = len(self.maze)
        self.maxc = len(self.maze[0])
        for r, line in enumerate(maze):
            if robot := line.strip("#."):
                self.pos = r, line.index(robot)
                self.dir = "^>v<".index(robot)
                break

    def front(self):
        return tuple(map(sum, zip(self.pos, self.FRONT[self.dir])))

    def safe(self):
        r, c = self.front()
        return (
            self.maze[r][c] == "#"
            if -1 < r < self.maxr and -1 < c < self.maxc
            else False
        )

    def turn(self):
        self.dir = (self.dir + 1) % 4
        if self.safe():
            self.actions.append("R")
            return True
        self.dir = (self.dir + 2) % 4
        if self.safe():
            self.actions.append("L")
            return True
        return False

    def move(self):
        steps = 0
        while self.safe():
            self.pos = self.front()
            steps += 1
        self.actions.append(str(steps))

    def path(self):
        self.turn()
        while True:
            self.move()
            if not self.turn():
                break
        return self.actions


def solve(data: str):
    prog = list(map(int, data.split(",")))
    write = []
    comp = Computer(prog, None, write.append)
    while comp.step():
        pass
    maze = "".join(map(chr, write)).strip().splitlines()
    path = Robot(maze).path()
    parts = set()
    for n in range(10, 2, -2):
        for i in range(0, len(path) - 2 * n, 2):
            actions = path[i : i + n]
            part = ",".join(actions)
            if len(part) > 20:
                continue
            for j in range(i + n, len(path) - n, 2):
                if path[j : j + n] == actions:
                    parts.add(part)
    path = ",".join(path)
    for a, b, c in combinations(parts, 3):
        if not path.replace(a, "").replace(b, "").replace(c, "").replace(",", ""):
            break
    m = path.replace(a, "A").replace(b, "B").replace(c, "C")
    read = list(reversed(list(map(ord, "\n".join([m, a, b, c]) + "\nn\n"))))
    comp = Computer(prog, read.pop, write.append)
    comp.mem[0] = 2
    while comp.step():
        pass
    return write[-1]


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
