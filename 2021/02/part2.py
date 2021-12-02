#!/usr/bin/env python3

aim = 0
depth = 0
distance = 0
with open("input.txt", "r") as f:
    for line in f:
        (cmd, value) = line.rstrip().split()
        value = int(value)
        if cmd == "forward":
            distance += value
            depth += aim * value
        elif cmd == "up":
            aim -= value
        elif cmd == "down":
            aim += value

print(depth * distance)
