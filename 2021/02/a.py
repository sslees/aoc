#! /usr/bin/env python3

from parse import parse
import aocd


def solve(data: str):
    depth = 0
    pos = 0
    for l in data.splitlines():
        com, amt = parse("{:l} {:d}", l)
        if com == "forward":
            pos += amt
        elif com == "down":
            depth += amt
        elif com == "up":
            depth -= amt
    return depth * pos


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    aocd.submit(answer, part="a", day=2, year=2021)
