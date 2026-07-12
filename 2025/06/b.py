#! /usr/bin/env python3

from itertools import zip_longest

import aocd
from parse import parse


def solve(data: str):
    numbers = list(zip_longest(*data.splitlines()[:-1], fillvalue=" "))
    operators = data.splitlines()[-1].split()
    total = 0
    op = operators.pop()
    current = 1 if op == "*" else 0
    while numbers:
        n = "".join(numbers.pop()).replace(" ", "")
        if n:
            if op == "*":
                current *= int(n)
            else:
                current += int(n)
        else:
            total += current
            op = operators.pop()
            current = 1 if op == "*" else 0
    total += current
    return total


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    aocd.submit(answer, part="b", day=6, year=2025)
