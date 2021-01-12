#! /usr/bin/env python3

orbits = {}

with open("examples-2.txt") as f:
    you = set()
    san = set()
    for l in f.readlines():
        inner, outer = l.strip().split(")")
        orbits[outer] = inner
    current = "YOU"
    while current in orbits:
        current = orbits[current]
        you.add(current)
    current = "SAN"
    while current in orbits:
        current = orbits[current]
        san.add(current)
    print(len(you.symmetric_difference(san)))
