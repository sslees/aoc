#! /usr/bin/env python3

import aocd


def solve(data: str):
    return max(sum([int(i) for i in e.split("\n")]) for e in data.split("\n\n"))


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    aocd.submit(answer, part="a", day=1, year=2022)
