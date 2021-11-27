#! /bin/env python3


def main(data: str):
    lines = [l.strip() for l in data.splitlines()]
    for l in lines:
        print(l)
    return 0


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(main(data))