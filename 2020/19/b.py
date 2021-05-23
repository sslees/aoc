#! /bin/env python3

from functools import cache
from itertools import product
import re


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


with open("input.txt") as f:
    rule, msgs = f.read().split("\n\n")
rules = {}
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
print(len(matches))
