#! /usr/bin/env python3

import aocd


def solve(data: str):
    data = [int(l) for l in data.splitlines()]
    answer = 0
    for i in range(len(data) - 3):
        if sum(data[i + 1 : i + 4]) > sum(data[i : i + 3]):
            answer += 1
    return answer


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    aocd.submit(answer, part="b", day=1, year=2021)
