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

    def __str__(self):
        return ('pos=<x={: 3}, y={: 3}, z={: 3}>, ' +
                'vel=<x={: 3}, y={: 3}, z={: 3}>').format(
                    self.x, self.y, self.z, self.dx, self.dy, self.dz)

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
        return (abs(self.x) + abs(self.y) + abs(self.z)) * \
            (abs(self.dx) + abs(self.dy) + abs(self.dz))


def main():
    moons = []
    with open('input.txt') as f:
        for l in f.readlines():
            match = re.match(r"<x=(-?\d+), y=(-?\d+), z=(-?\d+)>\n", l)
            moons.append(Moon(*map(int, match.groups())))
    for _ in range(1000):
        for moon, other in combinations(moons, 2):
            moon.apply_gravity(other)
        for moon in moons:
            moon.apply_velocity()
    print(sum([moon.energy() for moon in moons]))


if __name__ == '__main__':
    main()
