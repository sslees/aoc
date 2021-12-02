#! /usr/bin/env python3


def solve(data: str):
    dx = 3
    dy = 1
    m = [l.strip() for l in data.splitlines()]
    x = 0
    y = 0
    mx = len(m[1])
    my = len(m)
    count = 0
    while y < my:
        if m[y][x] == "#":
            count += 1
        x += dx
        x = x % mx
        y += dy
    return count


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
