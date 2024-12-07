#! /usr/bin/env python3


def solve(data: str):
    nums = [int(s) for s in data.split()]
    lefts = sorted(n for i, n in enumerate(nums) if i % 2 == 0)
    rights = sorted(n for i, n in enumerate(nums) if i % 2 != 0)
    return sum(l * rights.count(l) for l in lefts)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
