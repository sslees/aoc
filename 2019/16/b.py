#! /bin/env python3

from itertools import accumulate, cycle, islice, repeat
from operator import mod


def main():
    with open("input.txt") as f:
        data = [int(c) for c in f.readline().strip()]
    offset = int("".join(map(str, data[:7])))
    signal = reversed(list(islice(cycle(data), offset, len(data) * 10_000)))
    for _ in range(100):
        signal = map(mod, accumulate(signal), repeat(10))
    print("".join(map(str, list(signal)[-1:-9:-1])))


if __name__ == "__main__":
    main()
