from collections import defaultdict
from itertools import zip_longest

GLYPHS = {
    ".##..#..#.#..#.####.#..#.#..#.": "A",
    "###..#..#.###..#..#.#..#.###..": "B",
    ".##..#..#.#....#....#..#..##..": "C",
    "####.#....###..#....#....####.": "E",
    "####.#....###..#....#....#....": "F",
    ".##..#..#.#....#.##.#..#..###.": "G",
    "#..#.#..#.####.#..#.#..#.#..#.": "H",
    ".###...#....#....#....#...###.": "I",
    "..##....#....#....#.#..#..##..": "J",
    "#..#.#.#..##...#.#..#.#..#..#.": "K",
    "#....#....#....#....#....####.": "L",
    ".##..#..#.#..#.#..#.#..#..##..": "O",
    "###..#..#.#..#.###..#....#....": "P",
    "###..#..#.#..#.###..#.#..#..#.": "R",
    ".###.#....#.....##.....#.###..": "S",
    "#..#.#..#.#..#.#..#.#..#..##..": "U",
    "#...##...#.#.#...#....#....#..": "Y",
    "####....#...#...#...#....####.": "Z",
}


def scan(pic):
    if isinstance(pic, list):
        pic = "\n".join("".join("#" if c else "." for c in r) for r in pic)
    elif isinstance(pic, dict):
        chars = defaultdict(lambda: ".", {p: "#" for p, v in pic.items() if v})
        xs, ys = list(zip(*chars))
        xs, ys = range(min(xs), max(xs) + 1), range(max(ys), min(ys) - 1, -1)
        pic = "\n".join("".join(chars[x, y] for x in xs) for y in ys)
    ls = pic.strip().splitlines()
    ls = [["".join(s) for s in zip_longest(*(iter(l),) * 5, fillvalue=".")] for l in ls]
    return "".join([GLYPHS[c] for c in map("".join, zip(*ls))])
