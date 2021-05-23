#! /bin/env python3

CUPS = 1_000_000
MOVES = 10_000_000


def main():
    with open("input.txt") as f:
        cups = [int(c) for c in f.readline().strip()]
    after = {}
    cur = CUPS
    for cup in cups:
        after[cur] = cup
        cur = cup
    for cup in range(max(cups) + 1, CUPS + 1):
        after[cur] = cup
        cur = cup
    for _ in range(MOVES):
        cur = after[cur]
        up = [a := after[cur], b := after[a], c := after[b]]
        after[cur] = after[c]
        dest = cur
        while dest == cur or dest in up:
            dest = dest - 1 if dest > 1 else CUPS
        after[c] = after[dest]
        after[dest] = a
    print(after[1] * after[after[1]])


if __name__ == "__main__":
    main()
