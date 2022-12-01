#! /usr/bin/env python3

import aocd


def solve(data: str):
    return sum(
        int(len(d) in (2, 4, 3, 7))
        for l in data.splitlines()
        for d in l.split(" | ")[1].split()
    )


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    aocd.submit(answer, part="a", day=8, year=2021)
