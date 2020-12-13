#! /usr/bin/env python3

with open('input.txt') as f:
    data = f.readline()
    for noun in range(0, 99):
        for verb in range(0, 99):
            codes = data.split(',')
            codes[1:3] = noun, verb
            for pos in range(0, len(codes), 4):
                op = int(codes[pos])
                if op == 99:
                    if codes[0] == 19690720:
                        print(noun * 100 + verb)
                    break
                in1 = int(codes[pos + 1])
                in2 = int(codes[pos + 2])
                out = int(codes[pos + 3])
                if op == 1:
                    codes[out] = int(codes[in1]) + int(codes[in2])
                elif op == 2:
                    codes[out] = int(codes[in1]) * int(codes[in2])
