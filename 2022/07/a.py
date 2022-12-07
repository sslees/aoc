#! /usr/bin/env python3

import aocd
from parse import parse


def usage(path: str, sizes: dict[str, int]) -> int:
    return sum(sizes[s] for s in sizes if s.startswith(path + "/"))


def solve(data: str):
    cwd = []
    dirs = {"/"}
    sizes = {}
    for l in data.splitlines():
        if l == "$ cd /":
            cwd.clear()
        elif l == "$ cd ..":
            cwd.pop()
        elif l.startswith("$ cd"):
            cwd.append(l.split()[-1])
        elif l.startswith("dir"):
            dirs.add(("/" + "/".join(cwd) if cwd else "") + "/" + l.split()[1])
        elif l != "$ ls":
            size, file = parse("{:d} {}", l)
            sizes[("/" + "/".join(cwd) if cwd else "") + "/" + file] = size
    return sum(u for d in dirs if (u := usage(d, sizes)) < 100_000)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    aocd.submit(answer, part="a", day=7, year=2022)
