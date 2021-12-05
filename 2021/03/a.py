#! /usr/bin/env python3

import aocd


def solve(data: str):
    lines = data.splitlines()
    g = int("".join(max("10", key=c.count) for c in zip(*lines)), 2)
    e = ~g & ((1 << len(lines[0])) - 1)
    return g * e


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    aocd.submit(answer, part="a", day=3, year=2021)
