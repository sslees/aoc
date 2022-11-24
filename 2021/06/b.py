#! /usr/bin/env python3

from collections import defaultdict

import aocd


def solve(data: str):
    fish = [int(s) for s in data.split(",")]
    hist = defaultdict(int)
    diffs = defaultdict(int)
    for i in range(1, 257):
        if i < 11:
            for j in reversed(range(len(fish))):
                if fish[j] == 0:
                    fish.append(8)
                fish[j] += -1 if fish[j] else 6
            hist[i] = len(fish)
            diffs[i] = hist[i] - hist[i - 1]
        else:
            diffs[i] = diffs[i - 7] + diffs[i - 9]
            hist[i] = hist[i - 1] + diffs[i]
    return hist[i]


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    aocd.submit(answer, part="b", day=6, year=2021)
