#! /bin/env python3

import re


def containers(outers, inner, seen=[]):
    ret = outers[inner]
    for r in ret:
        if r in outers and r not in seen:
            seen.append(r)
            ret.extend(containers(outers, r, seen))
    return list(set(ret))


def solve(data: str):
    lines = data.splitlines()
    rules = {}
    for line in lines:
        outer, inners = re.match(r"(.+) bags contain (.+)\.", line).groups()
        inners = inners.split(", ")
        for i, inner in enumerate(inners):
            count, color = re.match(r"(\d+|no) (.+) bags?", inner).groups()
            inners[i] = (int(count.replace("no", "0")), color)
        rules[outer] = inners
    outers = {
        inner: []
        for inner in set([inner[1] for inners in rules.values() for inner in inners])
    }
    for outer, inners in rules.items():
        for inner in inners:
            outers[inner[1]].append(outer)
    return len(containers(outers, "shiny gold"))


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
