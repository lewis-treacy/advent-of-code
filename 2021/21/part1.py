#!/usr/bin/env python3

from itertools import cycle, islice

WIN = 1000

def mod10(x):
    return ((x-1)%10)+1

with open("input.txt", "r") as f:
    positions = [int(l.rstrip().split()[-1]) for l in f]

die = cycle(range(1, 101))

rolls = 0
scores = [0, 0]
while True:
    positions[0] = mod10(positions[0] + sum(islice(die, 3)))
    scores[0] += positions[0]
    rolls += 3
    if scores[0] >= WIN:
        print(scores[1] * rolls)
        break

    positions[1] = mod10(positions[1] + sum(islice(die, 3)))
    scores[1] += positions[1]
    rolls += 3
    if scores[1] >= WIN:
        print(scores[0] * rolls)
        break
