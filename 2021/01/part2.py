#!/usr/bin/env python3

#Input pre-processing
with open("input.txt", "r") as f:
    depths = list(map(int, f.readlines()))

windows = zip(depths[2:], depths[1:], depths)
window_sums = list(map(sum, windows))

increases = sum(map(lambda x: x[0] > x[1], zip(window_sums[1:], window_sums)))
print(increases)
