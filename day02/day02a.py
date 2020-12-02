#! /bin/env python3

import itertools

def main():
    with open("input.txt") as f:
        count = 0
        for line in f.readlines():
            line = line.rstrip()
            policy, passwd = line.split(": ")
            reps, letter = policy.split()
            low, high = reps.split("-")
            if int(low) <= passwd.count(letter) <= int(high):
                count += 1
    print(count)

if __name__ == "__main__":
    main()
