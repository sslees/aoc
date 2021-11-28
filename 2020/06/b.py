#! /bin/env python3


def solve(data: str):
    s = 0
    for g in data.split("\n\n"):
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
    return s


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
