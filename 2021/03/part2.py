#!/usr/bin/env python3

with open("input.txt", "r") as f:
    data = [int(x, 2) for x in f]

length = max(x.bit_length() for x in data)

o2 = [*data]
for i in range(length, -1, -1):
    bit = sum((x >> i) & 1 for x in o2) >= len(o2) / 2
    o2 = list(filter(lambda x: (x >> i) & 1 == bit, o2)) or o2

co2 = [*data]
for i in range(length, -1, -1):
    bit = sum((x >> i) & 1 for x in co2) < len(co2) / 2
    co2 = list(filter(lambda x: (x >> i) & 1 == bit, co2)) or co2

print(o2[0] * co2[0])
