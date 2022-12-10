#! /usr/bin/env python3

import aocd
from parse import parse

import utils.ocr as ocr


def tick(clk: int, reg: int, txt: str):
    txt += "\n" if clk % 40 == 1 else ""
    return txt + ("#" if ((clk - 1) % 40) in range(reg - 1, reg + 2) else "."), clk + 1


def solve(data: str):
    clk = 1
    reg = 1
    txt = ""
    for l in data.splitlines():
        if l == "noop":
            txt, clk = tick(clk, reg, txt)
        elif l.startswith("addx"):
            (x,) = parse("addx {:d}", l)
            txt, clk = tick(clk, reg, txt)
            txt, clk = tick(clk, reg, txt)
            reg += x
    return ocr.scan(txt)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    aocd.submit(answer, part="b", day=10, year=2022)
