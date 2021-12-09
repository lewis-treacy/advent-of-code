#!/usr/bin/env python3

from functools import reduce
from operator import mul

# returns list of coordinates of adjacent positions
def get_adjacents(grid, x, y):
    adjacents = set()
    if x > 0:
        adjacents.add((x-1,y))
    if x < len(grid[y])-1:
        adjacents.add((x+1,y))
    if y > 0:
        adjacents.add((x,y-1))
    if y < len(grid)-1:
        adjacents.add((x,y+1))

    return adjacents

def explore_basin(grid, x, y):
    basin = {(x,y)}
    adjacents = {(a, b) for a, b in get_adjacents(grid, x, y) if values[b][a] != 9 and values[b][a] > values[y][x]}

    for a, b in adjacents:
        basin.update(explore_basin(grid, a, b))
    return basin

with open("input.txt", "r") as f:
    values = [[int(c) for c in l.rstrip()] for l in f]

basins = []
for i in range(len(values)):
    for j in range(len(values[i])):
        value = values[i][j]
        adjacents = get_adjacents(values, j, i)
        if all(values[y][x] > values[i][j] for x, y in adjacents):
            basins.append(explore_basin(values, j, i))

# print basin map
for i in range(len(values)):
    for j in range(len(values[i])):
        in_basin = any((j,i) in b for b in basins)
        if in_basin:
            print('\033[91m', end="")
        print(values[i][j], end="")
        if in_basin:
            print('\033[0m', end="")
    print()
print()

product = reduce(mul, sorted(map(len, basins))[-3:], 1)
print(product)
