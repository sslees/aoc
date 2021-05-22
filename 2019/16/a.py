#! /bin/env python3

from itertools import chain, cycle, repeat
from operator import mul


def pattern(i):
    pat = cycle(chain(*(repeat(e, i + 1) for e in [0, 1, 0, -1])))
    next(pat)
    return pat


def main():
    with open("input.txt") as f:
        data = [int(c) for c in f.readline().strip()]
    for _ in range(100):
        data = [abs(sum(map(mul, data, pattern(i)))) % 10 for i in range(len(data))]
    print("".join(map(str, data[:8])))


if __name__ == "__main__":
    main()
