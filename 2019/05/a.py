#! /usr/bin/env python3

with open('input.txt') as f:
    mem = list(map(int, f.readline().split(',')))
    pc = 0
    while True:
        instr = '{:05}'.format(mem[pc])
        op = int(instr[-2:])
        m3, m2, m1 = list(map(int, instr[:-2]))
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
            mem[p1] = int(input('> '))
            pc += 2
        elif op == 4:
            p1 = mem[pc + 1] if m1 else mem[mem[pc + 1]]
            print(p1)
            pc += 2
