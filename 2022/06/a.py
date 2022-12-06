#! /usr/bin/env python3

import aocd

CT = 4


def solve(data: str):
    for i in range(len(data) - CT + 1):
        if len(set(data[i : i + CT])) == CT:
            return i + CT


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    aocd.submit(answer, part="b", day=6, year=2022)
