#!/usr/bin/env python3

with open("input.txt", "r") as f:
    numbers = list(map(int,f.readline().rstrip().split(',')))
    grids = [[[int(x) for x in l.split()] for l in g.split('\n')] for g in f.read().strip().split('\n\n')]

# Set up each grid to be a list of all possible winning sequences
# i.e. add the columns
for g in grids:
    extras = []
    # Add columns
    for i in range(len(g[0])):
        extras.append([l[i] for l in g])

    g += extras

for i in range(len(grids[0][0]), len(numbers)):
    check = numbers[:i]
    new_grids = [g for g in grids if not any([all([x in check for x in l]) for l in g])]

    if len(new_grids) == 0:
        g = grids[0]
        grid_sum = sum([sum([x for x in l if x not in check]) for l in g[:len(g[0])]])
        print(grid_sum * check[-1])
        break

    grids = new_grids
