#! /usr/bin/env python3

from parse import search


def check(s):
    adjacent = False
    ascending = True
    for i in range(5):
        if (
            s[i] == s[i + 1]
            and (i < 1 or s[i] != s[i - 1])
            and (i > 3 or s[i] != s[i + 2])
        ):
            adjacent = True
            break
    for i in range(5):
        if int(s[i]) > int(s[i + 1]):
            ascending = False
            break
    return adjacent and ascending


with open("input.txt") as f:
    data = f.readline()
count = 0
a, b = search("{:d}-{:d}", data)
for p in range(a, b):
    if check(str(p)):
        count += 1
print(count)
