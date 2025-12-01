#! /usr/bin/env python3

import math

from parse import parse


def solve(data: str):
    coins = 0
    for machine in data.split("\n\n"):
        lines = machine.splitlines()
        ax, ay = parse("Button A: X+{:d}, Y+{:d}", lines[0])
        bx, by = parse("Button B: X+{:d}, Y+{:d}", lines[1])
        px, py = parse("Prize: X={:d}, Y={:d}", lines[2])
        px, py = px + 10000000000000, py + 10000000000000
        lcm = math.lcm(ax, bx)
        b = 0
        for r in range(px % bx, lcm, bx):
            if r % ax == 0:
                a = r // ax
                b = (px - r) // bx
                break
        if b == 0:
            continue
        da = lcm // ax
        db = lcm // bx
        dy = da * ay - db * by
        off = py - a * ay - b * by
        if off % dy == 0:
            steps = off // dy
            a += steps * da
            b -= steps * db
            coins += a * 3 + b
    return coins


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
