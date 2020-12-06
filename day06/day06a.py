#! /bin/env python3


def main():
    with open("input.txt") as f:
        groups = f.read().split("\n\n")
    s = 0
    for g in groups:
        qs = set()
        for p in g.split("\n"):
            for q in p:
                qs.add(q)
        s += len(qs)
    print(s)


if __name__ == "__main__":
    main()
