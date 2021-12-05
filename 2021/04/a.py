#! /usr/bin/env python3

import aocd


def solve(data: str):
    boards = data.split("\n\n")
    calls = [int(s) for s in boards.pop(0).split(",")]
    whens = {e: i for i, e in enumerate(calls)}
    rounds = []
    for i, board in enumerate(boards):
        board = [[int(s) for s in l.split()] for l in board.splitlines()]
        boards[i] = [e for r in board for e in r]
        board += list(map(list, zip(*board)))
        rounds.append(min(max(map(whens.get, r)) for r in board))
    round = min(rounds)
    called = calls[: round + 1]
    return sum(set(boards[rounds.index(round)]) - set(called)) * called[-1]


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    answer = solve(data)
    print(answer)
    aocd.submit(answer, part="a", day=4, year=2021)
