#! /bin/env python3


def solve(data: str):
    prog = data.splitlines()
    acc = 0
    ptr = 0
    seen = set()
    while True:
        if ptr in seen:
            break
        seen.add(ptr)
        ins, val = prog[ptr].split()
        val = int(val)
        if ins == "acc":
            acc += val
            ptr += 1
        elif ins == "jmp":
            ptr += val
        else:
            ptr += 1
    return acc


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().rstrip("\r\n")
    print(solve(data))
