#! /usr/bin/env python3


def solve(data: str):
    wires = []
    for line in data.splitlines():
        last = (0, 0)
        points = set()
        for segment in line.split(","):
            direction = segment[0]
            distance = int(segment[1:])
            if direction == "U":
                for _ in range(distance):
                    last = (last[0], last[1] + 1)
                    points.add(last)
            elif direction == "D":
                for _ in range(distance):
                    last = (last[0], last[1] - 1)
                    points.add(last)
            elif direction == "L":
                for _ in range(distance):
                    last = (last[0] - 1, last[1])
                    points.add(last)
            elif direction == "R":
                for _ in range(distance):
                    last = (last[0] + 1, last[1])
                    points.add(last)
        wires.append(points)
    return min(map(lambda p: abs(p[0]) + abs(p[1]), wires[0] & wires[1]))


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
