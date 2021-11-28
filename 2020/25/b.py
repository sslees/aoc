#! /bin/env python3


def solve(data: str):
    return 25


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
