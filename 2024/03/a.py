#! /usr/bin/env python3

import re


def solve(data: str):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    return sum(int(m[0]) * int(m[1]) for m in re.findall(pattern, data))


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
