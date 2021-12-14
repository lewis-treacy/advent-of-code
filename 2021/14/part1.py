#!/usr/bin/env python3

from collections import Counter
from itertools import chain

steps = 10

with open("input.txt", "r") as f:
    poly = f.readline()
    f.readline()

    rules = {}
    for l in f:
        a, b = l.rstrip().split(' -> ')
        rules[a] = b

for a in range(0, steps):
    new_poly = ""
    for i in range(0, len(poly)-1):
        new_poly += poly[i] + rules[poly[i:i+2]] if poly[i:i+2] in rules else poly[i]
    new_poly += poly[-1]
    poly = new_poly

poly_counter = Counter(chain(*poly.split())).most_common()
print(poly_counter[0][1] - poly_counter[-1][1])
