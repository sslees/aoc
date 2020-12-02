#! /bin/env python3

import itertools

def main():
    with open("input.txt") as f:
        for a, b, c in itertools.combinations(f.readlines(), 3):
            a = int(a)
            b = int(b)
            c = int(c)
            if a + b + c == 2020:
                print(a * b * c)

if __name__ == "__main__":
    main()
