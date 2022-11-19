#! /usr/bin/env python3

import re
from functools import cache
from itertools import product

rules = {}
msgs = None


@cache
def possible(i=0):
    return [p for p in _poss(int(i)) if p in msgs]


def _poss(i):
    opts = rules[i]
    if opts[0][0][0] == '"':
        yield opts[0][0][1]
    else:
        for opt in opts:
            for perm in product(*map(possible, opt)):
                yield "".join(perm)


def solve(data: str):
    global msgs

    rule, msgs = data.split("\n\n")

    for r in rule.split("\n"):
        i, r = r.split(": ")
        rules[int(i)] = [s.split() for s in r.split(" | ")]
    patt = "^((?:{}){{2,}})((?:{})+)$".format(
        "|".join(possible(42)), "|".join(possible(31))
    )
    matches = []
    for msg in msgs.split("\n"):
        m = re.match(patt, msg)
        if m and len(m.group(1)) > len(m.group(2)):
            matches.append(m.group(0))
    return len(matches)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
