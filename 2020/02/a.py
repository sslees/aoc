#! /bin/env python3


def solve(data: str):
    count = 0
    for line in data.splitlines():
        policy, passwd = line.split(": ")
        reps, letter = policy.split()
        low, high = reps.split("-")
        if int(low) <= passwd.count(letter) <= int(high):
            count += 1
    return count


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
