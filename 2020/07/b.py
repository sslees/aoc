#! /usr/bin/env python3

import re


def contents(rules, outer):
    return sum(
        inner[0] + inner[0] * contents(rules, inner[1])
        for inner in rules[outer]
        if inner[1] in rules
    )


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
    return contents(rules, "shiny gold")


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
