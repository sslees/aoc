#! /usr/bin/env python3

import textwrap

w, h = 25, 6
with open('input.txt') as f:
    layers = textwrap.wrap(f.readline().strip(), width=w * h)
layer = min(layers, key=lambda l: l.count('0'))
print(layer.count('1') * layer.count('2'))
