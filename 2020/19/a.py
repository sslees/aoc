#! /bin/env python3

from functools import cache
from itertools import product


@cache
def possible(i=0):
    return [p for p in _poss(int(i))]


def _poss(i):
    opts = rules[i]
    if opts[0][0][0] == '"':
        yield opts[0][0][1]
    else:
        for opt in opts:
            for perm in product(*map(possible, opt)):
                yield "".join(perm)


with open("input.txt") as f:
    rule, msgs = f.read().split("\n\n")
rules = {}
for r in rule.split("\n"):
    i, r = r.split(": ")
    rules[int(i)] = [s.split() for s in r.split(" | ")]
print(len(set(possible()) & set(msgs.split("\n"))))
