#! /bin/env python3


def nxt(m, r, c, sq):
    if sq == ".":
        return False, "."
    adj = []
    for dy, dx in [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]:
        vis = None
        y, x = r, c
        try:
            while vis not in ("L", "#"):
                y += dy
                x += dx
                if y < 0 or x < 0:
                    raise IndexError
                vis = m[y][x]
        except IndexError:
            continue
        adj.append(vis)
    if sq == "L":
        ch = adj.count("#") == 0
        return int(ch), "#" if ch else "L"
    if sq == "#":
        ch = adj.count("#") >= 5
        return int(ch), "L" if ch else "#"


# def pretty(m):
#     for r in m[1:-1]:
#         print("".join(r[1:-1]))
#     print()


def main():
    with open("input.txt") as f:
        m = [[c for c in l.strip()] for l in f.readlines()]
    for row in m:
        row.insert(0, ".")
        row.append(".")
    m.insert(0, ["." for _ in range(len(m[0]))])
    m.append(["." for _ in range(len(m[0]))])

    changes = None
    while changes != 0:
        changes = 0
        tmp = [["?" for sq in r] for r in m]
        for r, row in enumerate(m):
            for c, sq in enumerate(row):
                ch, tmp[r][c] = nxt(m, r, c, sq)
                changes += ch
        m = tmp

    print([sq for r in m for sq in r].count("#"))


if __name__ == "__main__":
    main()
