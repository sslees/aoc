#! /bin/env python3

def main():
    dx = 1
    dy = 2
    with open("test.txt") as f:
        m = [l.strip() for l in f.readlines()]
    x = 0
    y = 0
    mx = len(m[1])
    my = len(m)
    count = 0
    while y < my:
        if m[y][x] == '#':
            count += 1
        x += dx
        x = x % mx
        y += dy
    print(count)

if __name__ == "__main__":
    main()
