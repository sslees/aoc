#! /usr/bin/env python3

import math

import aocd


class Monkey:
    def __init__(self, m: list[str]) -> None:
        self.items = list(map(int, m[1].split(": ")[1].split(", ")))
        self.op = eval("lambda old: " + m[2].split("= ")[1])
        self.div = int(m[3].split("by ")[1])
        self.true = int(m[4].split("monkey ")[1])
        self.false = int(m[5].split("monkey ")[1])
        self.inspects = 0

    def throws(self):
        while self.items:
            new = self.op(self.items.pop()) % Monkey.lcm
            self.inspects += 1
            yield (new, self.true) if new % self.div == 0 else (new, self.false)


def solve(data: str):
    monkeys = [Monkey(m.splitlines()) for m in data.split("\n\n")]
    Monkey.lcm = math.lcm(*(m.div for m in monkeys))
    for _ in range(10_000):
        for monkey in monkeys:
            for new, dest in monkey.throws():
                monkeys[dest].items.append(new)
    a, b = sorted([m.inspects for m in monkeys])[-2:]
    return a * b


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    aocd.submit(answer, part="b", day=11, year=2022)
