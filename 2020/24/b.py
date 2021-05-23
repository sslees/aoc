#! /bin/env python3

from collections import defaultdict
import re
import utils.cells as cells


def main():
    with open("input.txt") as f:
        data = [l.strip() for l in f.readlines()]
    tiles = defaultdict(bool)
    for l in data:
        ds = re.findall(r"[ns]?[ew]", l.replace("nw", "new").replace("se", "swe"))
        tiles[ds.count("e") - ds.count("w"), ds.count("ne") - ds.count("sw")] ^= True
    auto = cells.Automaton(tiles, rule=([2], [1, 2]), neighborhood=cells.HEX)
    for _ in range(100):
        auto.step()
    print(auto.population())


if __name__ == "__main__":
    main()
