#!/usr/bin/env python3

from itertools import starmap

flips = [
    lambda x, y, z: (x, y, z),
    lambda x, y, z: (x, y, -z),
    lambda x, y, z: (x, -y, z),
    lambda x, y, z: (x, -y, -z),
    lambda x, y, z: (-x, y, z),
    lambda x, y, z: (-x, y, -z),
    lambda x, y, z: (-x, -y, z),
    lambda x, y, z: (-x, -y, -z)
]

rotations = [
    lambda x, y, z: (x, y, z),
    lambda x, y, z: (x, z, y),
    lambda x, y, z: (z, y, x),
    lambda x, y, z: (y, x, z),
    lambda x, y, z: (y, z, x),
    lambda x, y, z: (z, x, y),
]

with open("input.txt", "r") as f:
    scanners = [{tuple(int(x) for x in l.split(',')) for l in s.rstrip().split('\n')[1:]} for s in f.read().split('\n\n')]

found = [True] + [False] * (len(scanners)-1)
while True:
    if all(found):
        break
    for i1, s1 in enumerate(scanners):
        if not found[i1]:
            continue

        if all(found):
            break

        for i2, s2 in enumerate(scanners):
            if found[i2]:
                continue

            for flip in flips:
                if found[i2]:
                    break

                for rot in rotations:
                    if found[i2]:
                        break

                    s2_mod = set(starmap(flip, starmap(rot, s2)))

                    for x1, y1, z1 in s1:
                        if found[i2]:
                            break

                        for x2, y2, z2 in s2_mod:
                            if found[i2]:
                                break

                            dx, dy, dz = x1 - x2, y1 - y2, z1 - z2
                            translated = set((x + dx, y + dy, z + dz) for x, y, z in s2_mod)

                            if len(s1.intersection(translated)) >= 12:
                                print(f"Found {sum(found)}/{len(scanners)} | {i2} {flip(1,1,1)} {rot('x','y','z')}")
                                found[i2] = True
                                scanners[i2] = translated

print(len(set.union(*scanners)))
