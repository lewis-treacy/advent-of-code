#!/usr/bin/env python3

from collections import Counter

def intersection(cube1, cube2):
    ((x1,x2),(y1,y2),(z1,z2)) = cube1
    ((a1,a2),(b1,b2),(c1,c2)) = cube2

    x1 = max(x1,a1)
    x2 = min(x2,a2)
    y1 = max(y1,b1)
    y2 = min(y2,b2)
    z1 = max(z1,c1)
    z2 = min(z2,c2)

    if x1 <= x2 and y1 <= y2 and z1 <= z2:
        return ((x1,x2),(y1,y2),(z1,z2))

cubes = Counter()
with open("input.txt", "r") as f:
    for l in f:
        cmd, coords = l.rstrip().split()
        cube = tuple(tuple(int(x) for x in c[2:].split('..')) for c in coords.split(','))

        new_cubes = Counter()
        for old_cube, count in cubes.items():
            inter = intersection(cube, old_cube)
            if inter:
                new_cubes[inter] -= count

        if cmd == 'on':
            new_cubes[cube] += 1

        cubes.update(new_cubes)

print(sum((x2-x1+1)*(y2-y1+1)*(z2-z1+1)*count for ((x1,x2),(y1,y2),(z1,z2)), count in cubes.items()))
