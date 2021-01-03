#! /bin/env python3

CUPS = 1_000_000
MOVES = 10_000_000


class Node:
    def __init__(self, val, nxt):
        self.val = val
        self.nxt = nxt

    def __repr__(self):
        return "{}->{}".format(self.val, self.nxt.val)


def main():
    with open("input.txt") as f:
        cups = [int(c) for c in f.readline().strip()]
    cups.extend(c for c in range(len(cups) + 1, CUPS + 1))
    ndx = {}
    cur = None
    for c in cups[::-1]:
        cur = Node(c, cur)
        ndx[c] = cur
    ndx[cups[-1]].nxt = ndx[cups[0]]
    for _ in range(MOVES):
        pu = cur.nxt
        cur.nxt = pu.nxt.nxt.nxt
        dst = cur.val - 1
        while not dst or dst in (pu.val, pu.nxt.val, pu.nxt.nxt.val):
            if not dst:
                dst = CUPS + 1
            dst -= 1
        dst = ndx[dst]
        pu.nxt.nxt.nxt = dst.nxt
        dst.nxt = pu
        cur = cur.nxt
    cur = ndx[1].nxt
    print(cur.val * cur.nxt.val)


if __name__ == "__main__":
    main()
