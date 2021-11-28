#! /usr/bin/env python3


def solve(data: str):
    total = 0
    for line in data.splitlines():
        total += int(line) // 3 - 2
    return total


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
