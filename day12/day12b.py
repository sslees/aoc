#! /bin/env python3


def main():
    with open("input.txt") as f:
        lines = [l.strip() for l in f.readlines()]
    x, y = 0, 0
    wx, wy = 10, 1
    for l in lines:
        cmd, val = l[0], int(l[1:])
        if cmd == "N":
            wy += val
        if cmd == "S":
            wy -= val
        if cmd == "E":
            wx += val
        if cmd == "W":
            wx -= val
        if cmd == "L":
            if val == 90:
                t = wx
                wx = -wy
                wy = t
            if val == 180:
                wx *= -1
                wy *= -1
            if val == 270:
                t = wx
                wx = wy
                wy = -t
        if cmd == "R":
            if val == 90:
                t = wx
                wx = wy
                wy = -t
            if val == 180:
                wx *= -1
                wy *= -1
            if val == 270:
                t = wx
                wx = -wy
                wy = t
        if cmd == "F":
            x += wx * val
            y += wy * val
    print(abs(x) + abs(y))


if __name__ == "__main__":
    main()
