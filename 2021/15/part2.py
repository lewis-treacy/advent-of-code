#!/usr/bin/env python3

import heapq
import math

def get_neighbours(grid, pos):
    neighbours = set()
    for a, b in [[0,1],[0,-1],[1,0],[-1,0]]:
        nx = pos[0] + a
        ny = pos[1] + b
        if nx < 0 or nx >= len(grid[0]) or ny < 0 or ny >= len(grid):
            continue
        neighbours.add((nx,ny))
    return neighbours

with open("input.txt", "r") as f:
    grid = [[int(x) for x in l.rstrip()] for l in f]

height = len(grid)
width = len(grid[0])
for row in grid:
    for chunk in range(4):
        row += [((x + chunk) % 9) + 1 for x in row[:width]]

for chunk in range(4):
    for row in grid[:height]:
        grid.append([((x + chunk) % 9) + 1 for x in row])

# Dijkstra
start = (0,0)
distances = {pos: math.inf for pos in [(x, y) for x in range(len(grid[0])) for y in range(len(grid))]}
distances[start] = 0
heap = [(0, start)]
while heap:
    dist, pos = heapq.heappop(heap)
    for n in get_neighbours(grid, pos):
        x, y = n
        new_dist = dist + grid[y][x]
        if new_dist < distances[n]:
            distances[n] = new_dist
            heapq.heappush(heap, (new_dist, n))

print(distances[len(grid[0])-1, len(grid)-1])
