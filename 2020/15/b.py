#! /bin/env python3

TURNS = 30_000_000


def solve(data: str):
    data = [int(s) for s in data.split(",")]
    said = [0] * (TURNS - 1)
    for i, d in enumerate(data, 1):
        said[d] = i
    say = 0
    for turn in range(len(data) + 1, TURNS + 1):
        says = say
        say = turn - said[says] if said[says] else 0
        said[says] = turn
    return says


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
