#! /usr/bin/env python3

import aocd


def solve(data: str):
    grid = [list(map(int, l)) for l in data.splitlines()]
    w = len(grid[0])
    h = len(grid)
    scores = set()
    for r in range(h):
        for c in range(w):
            v = [0] * 4
            cur = grid[r][c]
            for vr in range(r - 1, -1, -1):
                v[0] += 1
                if grid[vr][c] >= cur:
                    break
            for vr in range(r + 1, h):
                v[1] += 1
                if grid[vr][c] >= cur:
                    break
            for cr in range(c - 1, -1, -1):
                v[2] += 1
                if grid[r][cr] >= cur:
                    break
            for cr in range(c + 1, w):
                v[3] += 1
                if grid[r][cr] >= cur:
                    break
            scores.add(v[0] * v[1] * v[2] * v[3])
    return max(scores)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    aocd.submit(answer, part="b", day=8, year=2022)
