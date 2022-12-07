#! /usr/bin/env python3

from itertools import zip_longest

import aocd
from parse import parse


def solve(data: str):
    start, moves = data.split("\n\n")
    stacks = [
        list(s.strip()[1:])
        for z in zip_longest(*start.splitlines(), fillvalue=" ")
        if (s := "".join(reversed(z)))[0].isnumeric()
    ]
    for l in moves.splitlines():
        n, c1, c2 = parse("move {:d} from {:d} to {:d}", l.strip())
        stacks[c2 - 1] += stacks[c1 - 1][-n:]
        stacks[c1 - 1] = stacks[c1 - 1][:-n]
    return "".join(s[-1] for s in stacks)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    aocd.submit(answer, part="b", day=5, year=2022)
