#! /usr/bin/env python3


def solve(data: str):
    data = data.splitlines()
    fst = int(data[0])
    snd = set(data[1].split(","))
    snd.remove("x")
    snd = set(map(int, snd))
    nxt = {}
    for e in snd:
        nxt[e] = (fst // e + 1) * e - fst
    bus = sorted(nxt, key=lambda e: nxt[e])[0]
    return bus * nxt[bus]


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
