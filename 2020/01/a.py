#! /bin/env python3

from itertools import combinations


def main():
    with open("input.txt") as f:
        for a, b in combinations(f.readlines(), 2):
            a = int(a)
            b = int(b)
            if a + b == 2020:
                print(a * b)


if __name__ == "__main__":
    main()
