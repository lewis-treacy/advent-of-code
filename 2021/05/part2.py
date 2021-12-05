#!/usr/bin/env python3

with open("input.txt", "r") as f:
    lines = [[[int(c) for c in p.split(',')] for p in l.split(' -> ')] for l in f.readlines()]

maxX = max([max(l[0][0], l[1][0]) for l in lines])
maxY = max([max(l[0][1], l[1][1]) for l in lines])

grid = [[0]*(maxX+1) for _ in range(maxY+1)]

for [[x1, y1], [x2, y2]] in lines:
    xdir = -1 if x1 > x2 else 1
    ydir = -1 if y1 > y2 else 1

    if x1 == x2:
        for y in range(y1, y2+ydir, ydir):
            grid[y][x1] += 1
        continue

    if y1 == y2:
        for x in range(x1, x2+xdir, xdir):
            grid[y1][x] += 1
        continue

    for x, y in zip(range(x1, x2+xdir, xdir), range(y1, y2+ydir, ydir)):
        grid[y][x] += 1

count = sum([len([x for x in l if x >= 2]) for l in grid])
print(count)
