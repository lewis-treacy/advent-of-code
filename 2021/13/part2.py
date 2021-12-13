#!/usr/bin/env python3

def print_points(points):
    height = max(y for _, y in points) + 1
    width = max(x for x, _ in points) + 1
    for i in range(0, height):
        for j in range(0, width):
            print('#' if (j, i) in points else '.', end='')
        print()

with open("input.txt", "r") as f:
    points = set()
    for l in f:
        if l == "\n":
            break
        points.add(tuple(map(int, l.split(','))))

    for l in f:
        split = l.split()[2].split("=")
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

        print_points(points)
        print()

    print_points(points)
