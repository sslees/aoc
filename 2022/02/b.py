#! /usr/bin/env python3

import aocd


def solve(data: str):
    cases = {
        "A X": 3 + 0,
        "A Y": 1 + 3,
        "A Z": 2 + 6,
        "B X": 1 + 0,
        "B Y": 2 + 3,
        "B Z": 3 + 6,
        "C X": 2 + 0,
        "C Y": 3 + 3,
        "C Z": 1 + 6,
    }
    return sum(cases[c] for c in data.splitlines())


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    aocd.submit(answer, part="b", day=2, year=2022)
