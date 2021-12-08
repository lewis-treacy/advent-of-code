#!/usr/bin/env python3

with open("input.txt", "r") as f:
    values = [l.split('|')[1].split() for l in f]

count = sum(len([a for a in l if len(a) in {2,3,4,7}]) for l in values)
print(count)
