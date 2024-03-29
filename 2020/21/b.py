#! /usr/bin/env python3

import re


def solve(data: str):
    data = data.splitlines()
    srcs = {}
    for l in data:
        ingrs, alrgs = re.match(r"(.+) \(contains (.+)\)", l).groups()
        ingrs, alrgs = ingrs.split(), alrgs.split(", ")
        for alrg in alrgs:
            if alrg in srcs:
                srcs[alrg] &= set(ingrs)
            else:
                srcs[alrg] = set(ingrs)
    while any((len(ingr) > 1 for ingr in srcs.values())):
        for alrg, ingr in srcs.items():
            if len(ingr) == 1:
                (ingr, *extra) = ingr
                assert not extra
                for a in set(srcs) - {alrg}:
                    if ingr in srcs[a]:
                        srcs[a].remove(ingr)
    return ",".join((next(iter(srcs[alrg])) for alrg in sorted(srcs)))


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
