#! /usr/bin/env python3

from textwrap import wrap

import utils.ocr as ocr


def solve(data: str):
    W, H = 25, 6
    layers = wrap(data, W * H)
    pic = "".join(map(lambda l: next(v for v in l if v != "2"), zip(*layers)))
    return ocr.scan("\n".join(wrap(pic, W)).replace("0", ".").replace("1", "#"))


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
