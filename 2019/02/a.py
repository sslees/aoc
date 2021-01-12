#! /usr/bin/env python3

with open("input.txt") as f:
    for line in f.readlines():
        codes = line.split(",")
        codes[1:3] = 12, 2
        for pos in range(0, len(codes), 4):
            op = int(codes[pos])
            if op == 99:
                print(codes[0])
                break
            in1 = int(codes[pos + 1])
            in2 = int(codes[pos + 2])
            out = int(codes[pos + 3])
            if op == 1:
                codes[out] = int(codes[in1]) + int(codes[in2])
            elif op == 2:
                codes[out] = int(codes[in1]) * int(codes[in2])
