#! /bin/env python3

from collections import deque
from operator import mul


def main():
    with open("input.txt") as f:
        p1, p2 = f.read().rstrip("\r\n").split("\n\n")
    p1 = deque(map(int, p1.removeprefix("Player 1:\n").split("\n")))
    p2 = deque(map(int, p2.removeprefix("Player 2:\n").split("\n")))
    while p1 and p2:
        c1 = p1.popleft()
        c2 = p2.popleft()
        if c1 > c2:
            p1.extend([c1, c2])
        else:
            p2.extend([c2, c1])
    win = p1 if p1 else p2
    print(sum(map(mul, win, range(len(win), 0, -1))))


if __name__ == "__main__":
    main()
