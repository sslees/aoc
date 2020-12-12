#! /bin/env python3


def main():
    with open("input.txt") as f:
        d = [int(l.strip()) for l in f.readlines()]
    target = 675280050
    for n in range(2, len(d) + 1):
        for i in range(len(d) - n + 1):
            seq = d[i : i + n]
            if sum(seq) == target:
                print(min(seq) + max(seq))


if __name__ == "__main__":
    main()
