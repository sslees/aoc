#! /usr/bin/env python3


def solve(data: str):
    count = 0
    for p in data.split("\n\n"):
        if (
            "byr" in p
            and "iyr" in p
            and "eyr" in p
            and "hgt" in p
            and "hcl" in p
            and "ecl" in p
            and "pid" in p
        ):
            count += 1
    return count


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
