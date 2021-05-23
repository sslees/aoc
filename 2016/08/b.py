#! /usr/bin/env python3

from parse import parse
import utils.ocr as ocr


def main():
    with open("input.txt") as f:
        data = [l.strip() for l in f.readlines()]
    MX, MY = 50, 6
    disp = [[0] * MX for _ in range(MY)]
    for l in data:
        if p := parse("rect {:d}x{:d}", l):
            w, h = p
            for y in range(h):
                for x in range(w):
                    disp[y][x] = 1
        elif p := parse("rotate row y={:d} by {:d}", l):
            y, n = p
            n %= MX
            disp[y] = disp[y][-n:] + disp[y][:-n]
        elif p := parse("rotate column x={:d} by {:d}", l):
            x, n = p
            n %= MY
            tmp = {}
            for y in range(MY):
                tmp[(y + n) % MY, x] = disp[y][x]
            for y, x in tmp:
                disp[y][x] = tmp[y, x]
    print(ocr.scan(disp))


if __name__ == "__main__":
    main()
