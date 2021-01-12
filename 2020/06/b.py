#! /bin/env python3


def main():
    with open("input.txt") as f:
        groups = f.read().split("\n\n")
    s = 0
    for g in groups:
        qs = set()
        for i, p in enumerate(g.strip().split("\n")):
            if i == 0:
                for q in p:
                    qs.add(q)
            else:
                for q in qs.copy():
                    if q not in p:
                        qs.remove(q)
        s += len(qs)
    print(s)


if __name__ == "__main__":
    main()
