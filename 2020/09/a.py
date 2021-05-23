#! /bin/env python3

from itertools import combinations


def main():
    with open("input.txt") as f:
        d = [int(l.strip()) for l in f.readlines()]
    pre = 25
    for i in range(pre, len(d)):
        if not any(
            [a != b and a + b == d[i] for a, b in combinations(d[i - pre : i], 2)]
        ):
            print(d[i])
            break


if __name__ == "__main__":
    main()
