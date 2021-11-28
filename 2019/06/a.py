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


def solve(data: str):
    count = 0
    for l in data.splitlines():
        inner, outer = l.split(")")
        orbits[outer] = inner
    for o in orbits:
        count += calc(o)
    return count


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
