#! /usr/bin/env python3

import statistics

import aocd


def solve(data: str):
    vals = sorted(int(s) for s in data.split(","))
    med = int(statistics.median(vals))
    return sum(abs(v - med) for v in vals)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    aocd.submit(answer, part="a", day=7, year=2021)
