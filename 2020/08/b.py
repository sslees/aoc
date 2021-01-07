#! /bin/env python3


def run(prog):
    acc = 0
    ptr = 0
    seen = set()
    while True:
        if ptr in seen:
            return None
        seen.add(ptr)
        ins, val = prog[ptr].split()
        val = int(val)
        if ins == "acc":
            acc += val
            ptr += 1
        elif ins == "jmp":
            ptr += val
        elif ptr == len(prog) - 1:
            return acc
        else:
            ptr += 1


def main():
    with open("input.txt") as f:
        prog = [l.strip() for l in f.readlines()]
    prog.append("nop 0")
    for i in range(len(prog)):
        tmp = prog.copy()
        if tmp[i].split()[0] == "jmp":
            tmp[i] = "nop " + tmp[i].split()[1]
        elif tmp[i].split()[0] == "nop":
            tmp[i] = "jmp " + tmp[i].split()[1]
        else:
            continue
        if acc := run(tmp):
            print(acc)


if __name__ == "__main__":
    main()
