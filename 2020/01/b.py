#! /bin/env python3

from itertools import combinations


def main():
    with open("input.txt") as f:
        for a, b, c in combinations(f.readlines(), 3):
            a = int(a)
            b = int(b)
            c = int(c)
            if a + b + c == 2020:
                print(a * b * c)


if __name__ == "__main__":
    main()
