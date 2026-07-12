#! /usr/bin/env python3


from itertools import zip_longest


def value(presses: dict, target):
    val = [0] * len(target)
    for button, count in presses.items():
        for pos in button:
            val[pos] += count
    return val


def pretty(presses: dict, target):
    val = value(presses, target)
    lines = [
        "#" * min(v, t) + ("." if t > v else "!") * abs(t - v)
        for v, t in zip(val, target)
    ]
    print("\n".join(reversed(list(map("".join, zip_longest(*lines, fillvalue=" "))))))


def solve(data: str):
    total = 0
    for l in data.splitlines():
        buttons, target = l.split("] ")[1].split(" {")
        buttons = [[int(i) for i in b[1:-1].split(",")] for b in buttons.split()]
        target = [int(i) for i in target[:-1].split(",")]

        print("line:", l)
        pretty({}, target)

        while True:


    print("total:", total)
    return total


if __name__ == "__main__":
    # with open("input.txt") as f:
    #     data = f.read().rstrip("\r\n")
    data = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""
    answer = solve(data)
    print(answer)
    # aocd.submit(answer, part="b", day=10, year=2025)
