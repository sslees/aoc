#! /bin/env python3

P = 20201227  # should add a prime checker...
G = 7


def tf(s, l):
    return pow(s, l, P)


def main():
    with open("input.txt") as f:
        ap, bp = [int(l.strip()) for l in f.readlines()]
    a = next(a for a in range(1, P) if tf(G, a) == ap)
    ea = tf(bp, a)
    print(ea)


if __name__ == "__main__":
    main()
