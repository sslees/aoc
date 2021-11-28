#! /bin/env python3

P = 20201227
G = 7


def solve(data: str):
    ap, bp = [int(l) for l in data.splitlines()]
    for a in range(1, P):
        p = pow(G, a, P)
        if p == ap:
            return pow(bp, a, P)
        if p == bp:
            return pow(ap, a, P)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
