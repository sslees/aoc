#! /usr/bin/env python3


def fuel_needed(mass):
    fuel = mass // 3 - 2
    if fuel > 0:
        return fuel + fuel_needed(fuel)
    return 0


with open('input.txt') as f:
    total = 0
    for line in f.readlines():
        total += fuel_needed(int(line))
    print(total)
