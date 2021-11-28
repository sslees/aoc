#! /usr/bin/env python3

from parse import parse


def check(s):
    for i in range(5):
        if int(s[i]) > int(s[i + 1]):
            return False
    for i in range(5):
        if s[i] == s[i + 1]:
            return True
    return False


def solve(data: str):
    a, b = parse("{:d}-{:d}", data)
    ct = 0
    for p in range(a, b):
        ct += check(str(p))
    return ct


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
