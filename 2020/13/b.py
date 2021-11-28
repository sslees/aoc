#! /bin/env python3

from itertools import count


def solve(data: str):
    sched = data.splitlines()[1].split(",")
    rs = {int(n): (int(n) - i) % int(n) for i, n in enumerate(sched) if n != "x"}
    ns = list(sorted(rs))

    n = ns.pop()
    r = rs[n]
    while ns:
        n2 = ns[-1]
        r2 = rs[n2]
        for t in count(r, n):
            if t % n2 == r2:
                r = t
                n *= n2
                ns.pop()
                break
    return r


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
