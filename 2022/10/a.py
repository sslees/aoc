#! /usr/bin/env python3

import aocd
from parse import parse


def solve(data: str):
    clk = 1
    reg = 1
    sigs = []
    for l in data.splitlines():
        if l == "noop":
            sigs.extend([clk * reg] if clk % 40 == 20 else [])
            clk += 1
        elif l.startswith("addx"):
            (x,) = parse("addx {:d}", l)
            sigs.extend([clk * reg] if clk % 40 == 20 else [])
            clk += 1
            sigs.extend([clk * reg] if clk % 40 == 20 else [])
            clk += 1
            reg += x
    return sum(sigs)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    aocd.submit(answer, part="a", day=10, year=2022)
