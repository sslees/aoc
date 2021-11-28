#! /usr/bin/env python3

from textwrap import wrap


def solve(data: str):
    W, H = 25, 6
    layer = min(wrap(data, W * H), key=lambda l: l.count("0"))
    return layer.count("1") * layer.count("2")


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
