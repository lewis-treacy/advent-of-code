#!/usr/bin/env python3

depth = 0
distance = 0
with open("input.txt", "r") as f:
    for line in f:
        (cmd, value) = line.rstrip().split()
        value = int(value)
        if cmd == "forward":
            distance += value
        elif cmd == "up":
            depth -= value
        elif cmd == "down":
            depth += value

print(depth * distance)
