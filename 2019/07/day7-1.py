#! /usr/bin/env python3

from functools import lru_cache
from itertools import permutations
import os
import sys

prog = None


@lru_cache(maxsize=None)
def compute(phase, signal=0):
    sr = sys.stdin
    sw = sys.stdout
    prfd, pwfd = os.pipe()
    sys.stdin = os.fdopen(prfd)
    sys.stdout = os.fdopen(pwfd, 'w')
    mem = prog.copy()
    pc = 0
    print(phase)
    print(signal)
    while True:
        instr = '{:05}'.format(mem[pc])
        op = int(instr[-2:])
        _, m2, m1 = list(map(int, instr[:-2]))
        if op == 99:
            break
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
    sys.stdout = sw
    res = int(sys.stdin.readline())
    sys.stdin = sr

    return res


if __name__ == '__main__':
    outs = set()
    with open('input.txt') as f:
        prog = list(map(int, f.readline().split(',')))
    for perm in permutations(range(5)):
        pA, pB, pC, pD, pE = perm
        sB = compute(pA)
        sC = compute(pB, sB)
        sD = compute(pC, sC)
        sE = compute(pD, sD)
        outs.add(compute(pE, sE))
    print(max(outs))
    # print(compute.cache_info())  # 47.5% hit rate
