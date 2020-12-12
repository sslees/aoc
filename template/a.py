#! /bin/env python3


def main():
    with open("test.txt") as f:
        d = [l.strip() for l in f.readlines()]
    for l in d:
        print(l)


if __name__ == "__main__":
    main()
