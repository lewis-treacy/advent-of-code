#!/usr/bin/env python3

steps = 100

def get_adjacent(grid, x, y):
    adjacents = set()
    for i in range(-1, 2):
        for j in range(-1, 2):
            if x+i >= 0 and x+i <= len(grid[0])-1 and y+j >= 0 and y+j <= len(grid)-1:
                adjacents.add((x+i,y+j))
    return adjacents

def should_flash(grid, x, y, flashed):
    if grid[y][x] > 9 and (x, y) not in flashed:
        flashed.add((x,y))
        adjacents = get_adjacent(grid, x, y)
        for a, b in adjacents:
            grid[b][a] += 1
        for a, b in adjacents:
            should_flash(grid, a, b, flashed)
    return flashed

with open("input.txt", "r") as f:
    grid = [[int(x) for x in l.rstrip()] for l in f]

total_flashes = 0
for i in range(0, steps):
    flashed = set()
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            grid[y][x] += 1
            should_flash(grid, x, y, flashed)

    for x, y in flashed:
        grid[y][x] = 0

    total_flashes += len(flashed)

print(total_flashes)
