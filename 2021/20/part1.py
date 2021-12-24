#!/usr/bin/env python3

STEPS = 2

with open("input.txt", "r") as f:
    lookup = [True if c == '#' else False for c in f.readline().rstrip()]
    f.readline()

    image = [[True if c == '#' else False for c in l.rstrip()] for l in f]

void = False
for step in range(STEPS):
    new_image = []
    for i in range(-1 ,len(image)+1):
        row = []
        for j in range(-1, len(image[0])+1):
            index = ""
            for x, y in [(-1, -1), (0, -1), (1, -1), (-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]:
                if i+y < 0 or i+y >= len(image) or j+x < 0 or j+x >= len(image[0]):
                    index += '1' if void else '0'
                else:
                    index += '1' if image[i+y][j+x] else '0'
            row.append(lookup[int(index, 2)])
        new_image.append(row)
    image = new_image
    void = lookup[-1] if void else lookup[0]

print(sum([sum(l) for l in image]))
