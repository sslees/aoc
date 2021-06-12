#! /bin/env python3


def main():
    with open("e1.txt") as f:
        data = [l[:-1] for l in f.readlines()]
    for l in data:
        print(f">>>{l}<<<")


if __name__ == "__main__":
    main()
