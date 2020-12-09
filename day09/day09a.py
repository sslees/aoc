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
            print(d[i])


if __name__ == "__main__":
    main()
