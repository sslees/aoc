#! /usr/bin/env python3

import aocd


class Fish:
    def __init__(self, timer):
        self.timer = timer

    def next(self):
        if self.timer == 0:
            self.timer = 6
            return Fish(8)
        else:
            self.timer -= 1
            return None


def solve(data: str):
    fish = []
    for i in [int(s) for s in data.split(",")]:
        fish.append(Fish(i))
    for _ in range(80):
        for f in reversed(fish):
            f2 = f.next()
            if f2 is not None:
                fish.append(f2)
    return len(fish)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    aocd.submit(answer, part="a", day=6, year=2021)
