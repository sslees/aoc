#! /bin/env python3


def sid(code):
    row = int(code[0:7].replace("F", "0").replace("B", "1"), 2)
    col = int(code[7:10].replace("L", "0").replace("R", "1"), 2)
    return row * 8 + col


def main():
    with open("input.txt") as f:
        codes = [l.strip() for l in f.readlines()]
    seats = set()
    for s in map(sid, codes):
        seats.add(s)
    (seat,) = {s for s in range(min(seats), max(seats) + 1)} - seats
    print(seat)


if __name__ == "__main__":
    main()
