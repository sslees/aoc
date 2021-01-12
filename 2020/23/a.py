#! /bin/env python3


def main():
    with open("input.txt") as f:
        cups = [int(c) for c in f.readline().strip()]
    n = len(cups)
    cur = cups[0]
    for _ in range(100):
        i = cups.index(cur)
        pu = (cups * 2)[i + 1 : i + 4]
        for c in pu:
            cups.remove(c)
        dest = cur - 1
        while dest and dest in pu:
            dest -= 1
        if not dest:
            dest = max(cups)
        d = cups.index(dest) + 1
        for c in reversed(pu):
            cups.insert(d, c)
        cur = cups[(cups.index(cur) + 1) % n]
    i = cups.index(1)
    print("".join(map(str, (cups * 2)[i + 1 : i + n])))


if __name__ == "__main__":
    main()
