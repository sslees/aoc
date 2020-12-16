#! /bin/env python3

import re


def main():
    with open("input.txt") as f:
        notes = f.read()
    rules = {}
    for bound in re.findall(r"[\w| ]+:[^\n]+", notes):
        name, rule = bound.split(": ")
        a, b = rule.split(" or ")
        a1, a2 = a.split("-")
        b1, b2 = b.split("-")
        a1, a2, b1, b2 = int(a1), int(a2), int(b1), int(b2)
        rules[name] = (
            lambda v=None, a1=a1, a2=a2, b1=b1, b2=b2: a1 <= v <= a2 or b1 <= v <= b2
        )

    nearby = re.search(r"nearby tickets:\n(\d+[,|\n])+", notes).group(0)
    nearby = map(int, re.findall(r"\d+", nearby))

    err = 0
    for v in nearby:
        if not any([f(v) for f in rules.values()]):
            err += v
    print(err)


if __name__ == "__main__":
    main()
