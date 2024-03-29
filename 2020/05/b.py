#! /usr/bin/env python3


def sid(code):
    row = int(code[0:7].replace("F", "0").replace("B", "1"), 2)
    col = int(code[7:10].replace("L", "0").replace("R", "1"), 2)
    return row * 8 + col


def solve(data: str):
    codes = data.splitlines()
    seats = set()
    for s in map(sid, codes):
        seats.add(s)
    (seat,) = {s for s in range(min(seats), max(seats) + 1)} - seats
    return seat


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
