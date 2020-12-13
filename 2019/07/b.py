#! /usr/bin/env python3

import itertools
import os
import sys

sr = sys.stdin
sw = sys.stdout
prfd, pwfd = os.pipe()
sys.stdin = os.fdopen(prfd)
sys.stdout = os.fdopen(pwfd, "w")


def compute(mem, pc, phase):
    if pc == 0:
        print(phase)
        print(int(input()))
    while True:
        instr = "{:05}".format(mem[pc])
        op = int(instr[-2:])
        _, m2, m1 = list(map(int, instr[:-2]))
        if op == 1:
            p1 = mem[pc + 1] if m1 else mem[mem[pc + 1]]
            p2 = mem[pc + 2] if m2 else mem[mem[pc + 2]]
            p3 = mem[pc + 3]
            mem[p3] = p1 + p2
            pc += 4
        elif op == 2:
            p1 = mem[pc + 1] if m1 else mem[mem[pc + 1]]
            p2 = mem[pc + 2] if m2 else mem[mem[pc + 2]]
            p3 = mem[pc + 3]
            mem[p3] = p1 * p2
            pc += 4
        elif op == 3:
            p1 = mem[pc + 1]
            mem[p1] = int(input())
            pc += 2
        elif op == 4:
            p1 = mem[pc + 1] if m1 else mem[mem[pc + 1]]
            print(p1)
            pc += 2

            return mem, pc, phase
        elif op == 5:
            p1 = mem[pc + 1] if m1 else mem[mem[pc + 1]]
            p2 = mem[pc + 2] if m2 else mem[mem[pc + 2]]
            pc = p2 if p1 else pc + 3
        elif op == 6:
            p1 = mem[pc + 1] if m1 else mem[mem[pc + 1]]
            p2 = mem[pc + 2] if m2 else mem[mem[pc + 2]]
            pc = p2 if p1 else pc + 3
        elif op == 7:
            p1 = mem[pc + 1] if m1 else mem[mem[pc + 1]]
            p2 = mem[pc + 2] if m2 else mem[mem[pc + 2]]
            p3 = mem[pc + 3]
            mem[p3] = 1 if p1 < p2 else 0
            pc += 4
        elif op == 8:
            p1 = mem[pc + 1] if m1 else mem[mem[pc + 1]]
            p2 = mem[pc + 2] if m2 else mem[mem[pc + 2]]
            p3 = mem[pc + 3]
            mem[p3] = 1 if p1 == p2 else 0
            pc += 4
        elif op == 99:
            return None


if __name__ == "__main__":
    with open("input.txt") as f:
        prog = list(map(int, f.readline().split(",")))
    vals = set()
    for perm in itertools.permutations(range(5, 10)):
        pipeline = [(prog.copy(), 0, p) for p in perm]
        inds = itertools.cycle(range(len(pipeline)))
        print(0)
        while any(pipeline):
            i = next(inds)
            pipeline[i] = compute(*pipeline[i])
        vals.add(int(input()))
    sys.stdin = sr
    sys.stdout = sw
    print(max(vals))
