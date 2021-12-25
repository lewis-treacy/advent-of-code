#!/usr/bin/env python3

east = set()
south = set()
width = height = 0
with open("input.txt", "r") as f:
    for y, l in enumerate(f):
        l = l.rstrip()
        height += 1
        width = len(l)
        for x, c in enumerate(l):
            if c == '>':
                east.add((x,y))
            elif c == 'v':
                south.add((x,y))

steps = 0
while True:
    new_east = set()
    for (x,y) in east:
        new_pos = ((x+1) % width, y)
        if new_pos in east or new_pos in south:
            new_east.add((x,y))
        else:
            new_east.add(new_pos)

    new_south = set()
    for (x,y) in south:
        new_pos = (x, (y+1) % height)
        if new_pos in new_east or new_pos in south:
            new_south.add((x,y))
        else:
            new_south.add(new_pos)

    steps += 1
    if new_east == east and new_south == south:
        break
    east = new_east
    south = new_south

print(steps)
