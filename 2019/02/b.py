#! /usr/bin/env python3

from utils.intcode import Computer


def solve(data: str):
    prog = list(map(int, data.split(",")))
    for verb in range(100):
        for noun in range(100):
            comp = Computer(prog)
            comp.mem[1] = noun
            comp.mem[2] = verb
            while comp.step():
                pass
            if comp.mem[0] == 19690720:
                return 100 * noun + verb
                break


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
