#! /bin/env python3

import re
import collections


def main():
    with open("input.txt") as f:
        data = [l.strip() for l in f.readlines()]
    srcs = {}
    cts = collections.Counter()
    for l in data:
        ingrs, alrgs = re.match(r"(.+) \(contains (.+)\)", l).groups()
        ingrs, alrgs = ingrs.split(), alrgs.split(", ")
        for ingr in ingrs:
            cts[ingr] += 1
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
    for src in srcs.values():
        (ingr,) = src
        del cts[ingr]
    print(sum(cts.values()))


if __name__ == "__main__":
    main()
