#! /usr/bin/env python3

from utils.intcode import Computer
import curses


class Game:
    def __init__(self):
        self.bricks = set()
        self.paddle = None
        self.ball = None

    def move(self):
        if self.paddle > self.ball:
            return -1  # left
        if self.paddle < self.ball:
            return 1  # right
        return 0  # neutral


def main(stdscr):
    with open("input.txt") as f:
        prog = list(map(int, f.readline().split(",")))
    game = Game()
    io = []
    comp = Computer(prog, game.move, io.append)
    comp.mem[0] = 2
    curses.curs_set(0)
    stdscr.clear()
    while comp.running:
        while len(io) < 3 and comp.running:
            comp.step()
        if not comp.running:
            break
        val, y, x = io.pop(), io.pop(), io.pop()
        if x == -1 and y == 0:
            game.score = val
            stdscr.addstr(0, 0, "score: {}".format(val))
        else:
            if val == 2:
                game.bricks.add((x, y))
            elif val == 3:
                game.paddle = x
            elif val == 4:
                game.ball = x
            stdscr.addch(y + 1, x, " #=To"[val])
        stdscr.refresh()
    return game.score


if __name__ == "__main__":
    print(curses.wrapper(main))