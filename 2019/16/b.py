#! /usr/bin/env python3

from itertools import accumulate, cycle, islice, repeat
from operator import mod


def solve(data: str):
    data = [int(c) for c in data]
    offset = int("".join(map(str, data[:7])))
    signal = reversed(list(islice(cycle(data), offset, len(data) * 10_000)))
    for _ in range(100):
        signal = map(mod, accumulate(signal), repeat(10))
    return "".join(map(str, list(signal)[-1:-9:-1]))


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
