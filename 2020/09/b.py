#! /bin/env python3

import itertools


def main():
    with open("input.txt") as f:
        d = [int(l.strip()) for l in f.readlines()]
    pre = 25
    for i in range(pre, len(d)):
        if not any(
            [
                a != b and a + b == d[i]
                for a, b in itertools.combinations(d[i - pre : i], 2)
            ]
        ):
            target = d[i]
            break
    for n in range(2, len(d) + 1):
        for i in range(len(d) - n + 1):
            seq = d[i : i + n]
            if sum(seq) == target:
                print(min(seq) + max(seq))


if __name__ == "__main__":
    main()
