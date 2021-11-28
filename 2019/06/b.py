#! /usr/bin/env python3

orbits = {}


def solve(data: str):
    you = set()
    san = set()
    for l in data.splitlines():
        inner, outer = l.split(")")
        orbits[outer] = inner
    current = "YOU"
    while current in orbits:
        current = orbits[current]
        you.add(current)
    current = "SAN"
    while current in orbits:
        current = orbits[current]
        san.add(current)
    return len(you.symmetric_difference(san))


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
