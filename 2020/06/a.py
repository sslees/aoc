#! /bin/env python3


def solve(data: str):
    s = 0
    for g in data.split("\n\n"):
        qs = set()
        for p in g.split("\n"):
            for q in p:
                qs.add(q)
        s += len(qs)
    return s


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
