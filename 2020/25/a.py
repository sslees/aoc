#! /bin/env python3

P = 20201227
G = 7


def main():
    with open("input.txt") as f:
        ap, bp = [int(l.strip()) for l in f.readlines()]
    for a in range(1, P):
        p = pow(G, a, P)
        if p == ap:
            print(pow(bp, a, P))
            break
        if p == bp:
            print(pow(ap, a, P))
            break


if __name__ == "__main__":
    main()
