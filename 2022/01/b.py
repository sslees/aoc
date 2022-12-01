#! /usr/bin/env python3

import aocd


def solve(data: str):
    return sum(
        sorted(sum([int(i) for i in e.split("\n")]) for e in data.split("\n\n"))[-3:]
    )


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    aocd.submit(answer, part="b", day=1, year=2022)
