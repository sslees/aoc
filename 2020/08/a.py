#! /bin/env python3


def main():
    with open("input.txt") as f:
        prog = [l.strip() for l in f.readlines()]
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
    print(acc)


if __name__ == "__main__":
    main()
