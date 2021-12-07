#!/usr/bin/env python3

with open("test.txt", "r") as f:
    positions = [int(a) for a in f.readline().split(',')]

min_pos = min(positions)
max_pos = max(positions)

cost = {}
for i in range(min_pos, max_pos+1):
    cost[i] = sum(list(map(lambda x: abs(x-i), positions)))

print(min(cost.values()))
