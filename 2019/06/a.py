#! /usr/bin/env python3

orbits = {}
indirects = {}


def calc(planet):
    if planet == "COM":
        return 0
    if planet in indirects:
        return indirects[planet]
    indirects[planet] = calc(orbits[planet]) + 1

    return indirects[planet]


with open("input.txt") as f:
    count = 0
    for l in f.readlines():
        inner, outer = l.strip().split(")")
        orbits[outer] = inner
    for o in orbits:
        count += calc(o)
    print(count)
