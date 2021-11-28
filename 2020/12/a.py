#! /bin/env python3


def solve(data: str):
    lines = data.splitlines()
    x, y = 0, 0
    d = 0
    for l in lines:
        cmd, val = l[0], int(l[1:])
        if cmd == "N":
            y += val
        if cmd == "S":
            y -= val
        if cmd == "E":
            x += val
        if cmd == "W":
            x -= val
        if cmd == "L":
            d += val
            d = (d + 360) % 360
        if cmd == "R":
            d -= val
            d = (d + 360) % 360
        if cmd == "F":
            if d == 0:
                x += val
            elif d == 90:
                y += val
            elif d == 180:
                x -= val
            elif d == 270:
                y -= val
    return abs(x) + abs(y)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
