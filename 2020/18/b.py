#! /bin/env python3

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


def main():
    with open("input.txt") as f:
        print(sum((calc(l.strip()) for l in f.readlines())))


if __name__ == "__main__":
    main()
