#! /usr/bin/env python3

import re


def calc(line):
    while "(" in line:
        paren = re.search(r"\([^\(\)]+\)", line).group(0)
        line = line.replace(paren, str(calc(paren[1:-1])))
    while "+" in line:
        oper = re.search(r"\d+ \+ \d+", line).group(0)
        line = line.replace(oper, str(eval(oper)), 1)
    while "*" in line:
        oper = re.search(r"\d+ \* \d+", line).group(0)
        line = line.replace(oper, str(eval(oper)), 1)
    return int(line)


def solve(data: str):
    return sum((calc(l) for l in data.splitlines()))


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
