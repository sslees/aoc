#! /usr/bin/env python3

import aocd


def cmp(l, r):
    if type(l) == type(r) == int:
        return -1 if l < r else 1 if l > r else 0
    elif type(l) == type(r) == list:
        for l2, r2 in zip(l, r):
            if (c2 := cmp(l2, r2)) != 0:
                return c2
        return cmp(len(l), len(r))
    else:
        return cmp([l], r) if type(l) == int else cmp(l, [r])


def solve(data: str):
    pairs = [map(eval, l.split("\n")) for l in data.split("\n\n")]
    return sum(i for i, (l, r) in enumerate(pairs, start=1) if cmp(l, r) < 0)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    aocd.submit(answer, part="a", day=13, year=2022)
