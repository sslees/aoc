#! /bin/env python3


def main():
    with open("input.txt") as f:
        js = sorted([int(l.strip()) for l in f.readlines()])
    js.insert(0, 0)
    js.append(max(js) + 3)
    diffs = [js[i + 1] - js[i] for i in range(len(js) - 1)]
    print(diffs.count(1) * diffs.count(3))


if __name__ == "__main__":
    main()
