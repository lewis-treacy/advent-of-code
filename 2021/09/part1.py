#!/usr/bin/env python3

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

with open("input.txt", "r") as f:
    values = [[int(c) for c in l.rstrip()] for l in f]

total = 0
for i in range(len(values)):
    for j in range(len(values[i])):
        value = values[i][j]
        adjacents = get_adjacents(values, j, i)
        if all(values[y][x] > values[i][j] for x, y in adjacents):
            total += value + 1

print(total)
