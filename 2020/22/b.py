#! /bin/env python3

from collections import deque
from operator import mul


def game(p1, p2):
    seen = set()
    while p1 and p2:
        h = hash((tuple(p1), tuple(p2)))
        if h in seen:
            return 1
        else:
            seen.add(h)
        c1 = p1.popleft()
        c2 = p2.popleft()
        if len(p1) >= c1 and len(p2) >= c2:
            win = game(deque(list(p1)[:c1]), deque(list(p2)[:c2]))
        else:
            win = 1 if c1 > c2 else 2
        if win == 1:
            p1.extend([c1, c2])
        else:
            p2.extend([c2, c1])
    return 1 if p1 else 2


def main():
    with open("input.txt") as f:
        p1, p2 = f.read().rstrip("\r\n").split("\n\n")
    p1 = deque(map(int, p1.removeprefix("Player 1:\n").split("\n")))
    p2 = deque(map(int, p2.removeprefix("Player 2:\n").split("\n")))
    win = p1 if game(p1, p2) == 1 else p2
    print(sum(map(mul, win, range(len(win), 0, -1))))


if __name__ == "__main__":
    main()
