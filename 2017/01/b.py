#! /usr/bin/env python3


def solve(data: str):
    ct = 0
    for i, c in enumerate(data):
        if c == data[(i + len(data) // 2) % len(data)]:
            ct += int(c)
    return ct


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
