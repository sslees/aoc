#! /usr/bin/env python3

from itertools import batched

import aocd


def solve(data: str):
    invalids = 0
    for r in data.replace("\n", "").split(","):
        a, b = r.split("-")
        for i in range(int(a), int(b) + 1):
            id = str(i)
            if invalid(id):
                invalids += int(id)
    return invalids


def invalid(id):
    idlen = len(id)
    for size in range(1, idlen // 2 + 1):
        if idlen % size == 0:
            if len(set(batched(id, size))) == 1:
                return True
    return False


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    aocd.submit(answer, part="b", day=2, year=2025)
