#!/usr/bin/env python3

with open("input.txt", "r") as f:
    points = set()
    for l in f:
        if l == "\n":
            break
        points.add(tuple(map(int, l.split(','))))

    split = f.readline().split()[2].split("=")
    direction = split[0]
    position = int(split[1])

    if direction == "x":
        a = {(x, y) for x, y in points if x < position}
        b = {(2 * position - x, y) for x, y in points if x > position}
        points = a.union(b)
    elif direction == "y":
        a = {(x, y) for x, y in points if y < position}
        b = {(x, 2 * position - y) for x, y in points if y > position}
        points = a.union(b)

    print(len(points))
