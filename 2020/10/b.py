#! /bin/env python3

from functools import cache
import math


@cache
def fib(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    if n == 2:
        return 4
    return fib(n - 1) + fib(n - 2) + fib(n - 3)


def main():
    with open("input.txt") as f:
        js = sorted([int(l.strip()) for l in f.readlines()])
    js.insert(0, 0)
    js.append(max(js) + 3)
    diffs = [js[i + 1] - js[i] for i in range(len(js) - 1)]
    counts = []
    ones = 0
    for diff in diffs:
        if diff == 3:
            if ones > 1:
                counts.append(ones - 1)
            ones = 0
        else:
            ones += 1
    print(math.prod([fib(i) for i in counts]))


if __name__ == "__main__":
    main()
