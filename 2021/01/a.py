#! /usr/bin/env python3

import aocd


def solve(data: str):
    data = [int(l) for l in data.splitlines()]
    answer = 0
    for i in range(len(data) - 1):
        if data[i + 1] > data[i]:
            answer += 1
    return answer


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    aocd.submit(answer, part="a", day=1, year=2021)
