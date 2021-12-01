#!/usr/bin/env python3

#Input pre-processing
with open("input.txt", "r") as f:
    depths = list(map(int, f.readlines()))

increases = sum(map(lambda x: x[0] > x[1], zip(depths[1:], depths)))

print(increases)
