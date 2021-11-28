#! /usr/bin/env python3


def fuel_needed(mass):
    fuel = mass // 3 - 2
    if fuel > 0:
        return fuel + fuel_needed(fuel)
    return 0


def solve(data: str):
    total = 0
    for line in data.splitlines():
        total += fuel_needed(int(line))
    return total


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
