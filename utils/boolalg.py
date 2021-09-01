from collections import defaultdict
from itertools import product
import math


def combine(rep1, rep2):
    diff = None
    for i in range(len(rep1)):
        if rep1[i] != rep2[i]:
            if diff is not None:
                return
            diff = i
    chars = list(rep1)
    chars[diff] = "x"
    return "".join(chars)


# 0,1,2,3,4,5,6,7,9,11,13
table = "x1x1x1x101010100"
# table = "0100110101010010"  # test
vars = int(math.sqrt(len(table)))
steps = [defaultdict(set)]
terms = {}
for term, val in enumerate(table):
    if val != "0":
        print(term, end=",")
        rep = f"{term:b}".zfill(vars)
        steps[0][rep.count("1")].add(rep)
        terms[rep] = {term}
prime = set()
while steps[-1]:
    steps.append(defaultdict(set))
    prime |= {rep for ones in steps[-2].values() for rep in ones}
    for ones in range(max(steps[-2])):
        for rep1, rep2 in product(steps[-2][ones], steps[-2][ones + 1]):
            if rep3 := combine(rep1, rep2):
                steps[-1][rep3.count("1")].add(rep3)
                terms[rep3] = terms[rep1] | terms[rep2]
                prime -= {rep1, rep2}
print(prime)
