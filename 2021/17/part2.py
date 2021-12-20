#!/usr/bin/env python3

def reaches_target(target, velocity):
    [[x1, x2], [y1, y2]] = target
    dx, dy = velocity

    x, y = 0, 0
    maxY = 0
    while x <= x2 and y >= y1:
        x += dx
        y += dy
        maxY = max(maxY, y)
        dx += -1 if dx > 0 else 1 if dx < 0 else 0
        dy -= 1

        if x >= x1 and x <= x2 and y >= y1 and y <= y2:
            return maxY

with open("input.txt", "r") as f:
    area = [[int(x) for x in r[2:].split('..')] for r in f.readline().rstrip().split(': ')[1].split(', ')]

solutions = 0
for dx in range(area[0][1] + 1):
    for dy in range(area[1][0], 200):
        y = reaches_target(area, (dx,dy))
        if y != None:
            solutions += 1

print(solutions)
