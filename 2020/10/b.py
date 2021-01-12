#! /bin/env python3

import functools
import math


# def valid(d):
#     ct = 0
#     for i in range(1, len(d) - 1):
#         a, _, c = d[i - 1 : i + 2]
#         if c - a <= 3:
#             ct += 1
#             o = d[i + 1 :]
#             o.insert(0, a)
#             ct += valid(o)
#     return ct


@functools.lru_cache()
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
    # print(valid(js) + 1)
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
