#! /bin/env python3

def id(code):
    row = int(code[0:7].replace('F', '0').replace('B', '1'), 2)
    col = int(code[7:10].replace('L', '0').replace('R', '1'), 2)
    return row * 8 + col

def main():
    with open("input.txt") as f:
        codes = [l.strip() for l in f.readlines()]
    print(max([id(code) for code in codes]))


if __name__ == "__main__":
    main()
