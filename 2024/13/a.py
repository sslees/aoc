#! /usr/bin/env python3

from itertools import product

from parse import parse

TRY = sorted(product(range(101), repeat=2), key=lambda amts: amts[0] * 3 + amts[1])


def solve(data: str):
    coins = 0
    for machine in data.split("\n\n"):
        lines = machine.splitlines()
        ax, ay = parse("Button A: X+{:d}, Y+{:d}", lines[0])
        bx, by = parse("Button B: X+{:d}, Y+{:d}", lines[1])
        px, py = parse("Prize: X={:d}, Y={:d}", lines[2])
        for a, b in TRY:
            if a * ax + b * bx == px and a * ay + b * by == py:
                coins += a * 3 + b
                break
    return coins


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
