#! /usr/bin/env python3

with open("input.txt") as f:
    wires = []
    for line in f.readlines():
        last = (0, 0)
        points = []
        for segment in line.split(","):
            direction = segment[0]
            distance = int(segment[1:])
            if direction == "U":
                for _ in range(distance):
                    last = (last[0], last[1] + 1)
                    points.append(last)
            elif direction == "D":
                for _ in range(distance):
                    last = (last[0], last[1] - 1)
                    points.append(last)
            elif direction == "L":
                for _ in range(distance):
                    last = (last[0] - 1, last[1])
                    points.append(last)
            elif direction == "R":
                for _ in range(distance):
                    last = (last[0] + 1, last[1])
                    points.append(last)
        wires.append(points)
    print(
        min(
            map(
                lambda p: wires[0].index(p) + wires[1].index(p) + 2,
                set(wires[0]) & set(wires[1]),
            )
        )
    )
