#! /usr/bin/env python3

from collections import Counter

import aocd

DIGLEN = {2: 1, 4: 4, 3: 7}
SEGFRQ = {9: "f", 6: "b", 4: "e"}
DIGITS = {
    "abcefg": "0",
    "cf": "1",
    "acdeg": "2",
    "acdfg": "3",
    "bcdf": "4",
    "abdfg": "5",
    "abdefg": "6",
    "acf": "7",
    "abcdefg": "8",
    "abcdfg": "9",
}


def solve(data: str):
    total = 0
    for l in data.splitlines():
        key = {}
        sigs, digs = [e.split() for e in l.split(" | ")]
        for sig in sigs:
            ct = len(sig)
            if 2 <= ct <= 4:
                key[DIGLEN[ct]] = set(sig)
        key[next(iter(key[7] - key[1]))] = "a"
        for s, n in Counter("".join(sigs)).items():
            if n == 7:
                key[s] = "g" if s not in key[4] else "d"
            elif n == 8:
                if s not in key:
                    key[s] = "c"
            else:
                key[s] = SEGFRQ[n]
        disps = [DIGITS["".join(sorted(map(key.get, d)))] for d in digs]  # type: ignore
        total += int("".join(disps))
    return total


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    aocd.submit(answer, part="b", day=8, year=2021)
