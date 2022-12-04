#! /usr/bin/env python3

import aocd
from parse import parse


def solve(data: str):
    ct = 0
    for l in data.splitlines():
        a, b, c, d = parse("{:d}-{:d},{:d}-{:d}", l)
        ct += int((a <= c and d <= b) or (c <= a and b <= d))
    return ct


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    aocd.submit(answer, part="a", day=4, year=2022)
