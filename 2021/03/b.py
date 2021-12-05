#! /usr/bin/env python3

import aocd


def ratings(lines, fn, opts, pos=0):
    bc = fn(opts, key=list(zip(*lines))[pos].count)
    lines = list(filter(lambda l: l[pos] == bc, lines))
    return lines[0] if len(lines) == 1 else ratings(lines, fn, opts, pos + 1)


def solve(data: str):
    lines = data.splitlines()
    o2 = int(ratings(lines, max, "10"), 2)
    co2 = int(ratings(lines, min, "01"), 2)
    return o2 * co2


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    aocd.submit(answer, part="b", day=3, year=2021)
