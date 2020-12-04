#! /bin/env python3

def main():
    with open("test.txt") as f:
        d = f.read()
    print(d)


if __name__ == "__main__":
    main()
