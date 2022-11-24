#! /usr/bin/env python3

import aocd


def solve(data: str):
    fish = [int(s) for s in data.split(",")]
    for _ in range(80):
        for i in reversed(range(len(fish))):
            if fish[i] == 0:
                fish.append(8)
            fish[i] += -1 if fish[i] else 6
    return len(fish)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    aocd.submit(answer, part="a", day=6, year=2021)
