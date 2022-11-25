#! /usr/bin/env python3

import aocd


def solve(data: str):
    vals = [int(s) for s in data.split(",")]
    return min(
        sum((n := abs(v - goal)) * (n + 1) // 2 for v in vals)
        for goal in range(min(vals), max(vals))
    )


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    aocd.submit(answer, part="b", day=7, year=2021)
