#! /usr/bin/env python3

with open("input.txt") as f:
    total = 0
    for line in f.readlines():
        total += int(line) // 3 - 2
    print(total)
