#! /bin/env python3

import itertools


def main():
    with open("input.txt") as f:
        fst = int(f.readline())
        snd = set([l.strip() for l in f.readline().split(",")])
        snd.remove("x")
        snd = set(map(int, snd))
    print(fst, snd)
    nxt = {}
    for e in snd:
        nxt[e] = (fst // e + 1) * e - fst
    bus = sorted(nxt, key=lambda e: nxt[e])[0]
    print(bus * nxt[bus])


if __name__ == "__main__":
    main()
