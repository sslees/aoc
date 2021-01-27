#! /usr/bin/env python3

from textwrap import wrap


def main():
    with open("input.txt") as f:
        data = f.readline().strip()
    W, H = 25, 6
    layer = min(wrap(data, W * H), key=lambda l: l.count("0"))
    print(layer.count("1") * layer.count("2"))


if __name__ == "__main__":
    main()
