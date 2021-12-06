#!/usr/bin/env python3

DAYS = 256

with open("input.txt", "r") as f:
    ages = [int(a) for a in f.readline().split(',')]

age_dict = {i: len(list(filter(lambda x: x == i, ages))) for i in range(0, 9)}

for i in range(DAYS):
    age_dict = {k-1: v for k,v in age_dict.items()}
    age_dict[6] += age_dict[-1]
    age_dict[8] = age_dict[-1]
    del age_dict[-1]

print(sum(age_dict.values()))
