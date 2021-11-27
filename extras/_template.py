#! /bin/env python3


def main():
    with open("e1.txt") as f:
        data = [l.strip() for l in f.readlines()]
    for l in data:
        print(l)


if __name__ == "__main__":
    main()
