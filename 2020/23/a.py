#! /bin/env python3

MOVES = 100


def main():
    with open("input.txt") as f:
        cups = [int(c) for c in f.readline().strip()]
    after = {}
    cur = cups[-1]
    for cup in cups:
        after[cur] = cup
        cur = cup
    for _ in range(MOVES):
        cur = after[cur]
        up = [a := after[cur], b := after[a], c := after[b]]
        after[cur] = after[c]
        dest = cur
        while dest == cur or dest in up:
            dest = dest - 1 if dest > 1 else max(cups)
        after[c] = after[dest]
        after[dest] = a
    order = [after[1]]
    for _ in range(len(cups) - 2):
        order.append(after[order[-1]])
    print("".join(map(str, order)))


if __name__ == "__main__":
    main()
