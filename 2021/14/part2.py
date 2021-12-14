#!/usr/bin/env python3

from collections import Counter, defaultdict

steps = 40

with open("input.txt", "r") as f:
    start = f.readline().rstrip()
    f.readline()

    rules = {}
    for l in f:
        a, b = l.rstrip().split(' -> ')
        rules[a] = b

poly = Counter([start[i:i+2] for i in range(0, len(start)-1)])
for a in range(0, steps):
    new_poly = Counter()
    for k, v in poly.items():
        if k in rules:
            m = rules[k]
            new_poly[k[0]+m] += v
            new_poly[m+k[1]] += v
        else:
            new_poly[k] += v
    poly = new_poly

letter_count = Counter()
for k, v in poly.items():
    letter_count[k[0]] += v
letter_count[start[-1]] += 1

counts = letter_count.values()
print(max(counts) - min(counts))
