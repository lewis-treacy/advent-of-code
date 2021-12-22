#!/usr/bin/env python3

cells = set()

with open("input.txt", "r") as f:
    for l in f:
        cmd, coords = l.rstrip().split()
        coords = [[int(x) for x in c[2:].split('..')] for c in coords.split(',')]

        for x in range(max(coords[0][0], -50), min(coords[0][1]+1 , 51)):
            for y in range(max(coords[1][0], -50), min(coords[1][1]+1 , 51)):
                for z in range(max(coords[2][0], -50), min(coords[2][1]+1 , 51)):
                    if cmd == 'on':
                        cells.add((x,y,z))
                    else:
                        if (x,y,z) in cells:
                            cells.remove((x,y,z))

print(len(cells))
