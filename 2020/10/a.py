#! /usr/bin/env python3


def solve(data: str):
    js = sorted([int(l) for l in data.splitlines()])
    js.insert(0, 0)
    js.append(max(js) + 3)
    diffs = [js[i + 1] - js[i] for i in range(len(js) - 1)]
    return diffs.count(1) * diffs.count(3)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
