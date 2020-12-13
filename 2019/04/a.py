#! /usr/bin/env python3


def check(s):
    adjacent = False
    ascending = True
    for i in range(5):
        if s[i] == s[i + 1]:
            adjacent = True
            break
    for i in range(5):
        if int(s[i]) > int(s[i + 1]):
            ascending = False
            break
    return adjacent and ascending


count = 0
for p in range(271973, 785961):
    if check(str(p)):
        count += 1
print(count)
