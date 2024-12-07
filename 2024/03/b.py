#! /usr/bin/env python3

import re


def solve(data: str):
    total = 0
    enabled = True
    for m in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\)|don't\(\))", data):
        if m[2]:
            enabled = m[2] == "do()"
        elif enabled:
            total += int(m[0]) * int(m[1])
    return total


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
