#! /usr/bin/env python3

from utils.intcode import Computer


class Game:
    def move(self):
        if self.paddle > self.ball:
            return -1  # left
        if self.paddle < self.ball:
            return 1  # right
        return 0  # neutral


def solve(data: str):
    prog = list(map(int, data.split(",")))
    game = Game()
    io = []
    comp = Computer(prog, game.move, io.append)
    comp.mem[0] = 2
    while comp.running:
        while len(io) < 3 and comp.running:
            comp.step()
        if not comp.running:
            break
        val, y, x = io.pop(), io.pop(), io.pop()
        if x == -1 and y == 0:
            score = val
        else:
            if val == 3:
                game.paddle = x
            elif val == 4:
                game.ball = x
    return score


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
