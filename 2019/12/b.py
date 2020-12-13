#! /usr/bin/env python3

from itertools import combinations
import re


class Moon:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.dx = 0
        self.dy = 0
        self.dz = 0

    def __hash__(self):
        return hash((self.x, self.y, self.z, self.dx, self.dy, self.dz))

    def __eq__(self, other):
        return (
            self.x == other.x
            and self.y == other.y
            and self.z == other.z
            and self.dx == other.dx
            and self.dy == other.dy
            and self.dz == other.dz
        )

    def __str__(self):
        return (
            "pos=<x={: 3}, y={: 3}, z={: 3}>, " + "vel=<x={: 3}, y={: 3}, z={: 3}>"
        ).format(self.x, self.y, self.z, self.dx, self.dy, self.dz)

    def apply_gravity(self, other):
        if self.x < other.x:
            self.dx += 1
            other.dx -= 1
        elif self.x > other.x:
            self.dx -= 1
            other.dx += 1
        if self.y < other.y:
            self.dy += 1
            other.dy -= 1
        elif self.y > other.y:
            self.dy -= 1
            other.dy += 1
        if self.z < other.z:
            self.dz += 1
            other.dz -= 1
        elif self.z > other.z:
            self.dz -= 1
            other.dz += 1

    def apply_velocity(self):
        self.x += self.dx
        self.y += self.dy
        self.z += self.dz

    def energy(self):
        return (abs(self.x) + abs(self.y) + abs(self.z)) * (
            abs(self.dx) + abs(self.dy) + abs(self.dz)
        )


def main():
    moons = []
    cache = set()
    # with open('example1p1.txt') as f:
    with open("test1p2.txt") as f:
        for l in f.readlines():
            match = re.match(r"<x=(-?\d+), y=(-?\d+), z=(-?\d+)>\n", l)
            moon = Moon(*map(int, match.groups()))
            moons.append(moon)
            print(moon)
    while True:
        h = hash(tuple(moons))
        if h in cache:
            break
        else:
            cache.add(h)
        for moon, other in combinations(moons, 2):
            moon.apply_gravity(other)
        for moon in moons:
            moon.apply_velocity()
        print(sum([moon.energy() for moon in moons]))
    print("steps: {}\n".format(len(cache)))


if __name__ == "__main__":
    main()
