#!/usr/bin/env python3

DAYS = 80

with open("input.txt", "r") as f:
    ages = [int(a) for a in f.readline().split(',')]

for i in range(DAYS):
    new_count = len(list(filter(lambda a: a == 0, ages)))
    ages = list(map(lambda a: a-1 if a>0 else 6, ages))
    ages += [8]*new_count

print(len(ages))
