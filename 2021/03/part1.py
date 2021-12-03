#!/usr/bin/env python3

with open("input.txt", "r") as f:
    data = [int(x, 2) for x in f]

length = max(x.bit_length() for x in data)

gamma = 0
for i in range(length):
    gamma_bit = sum((x >> i) & 1 for x in data) > len(data) // 2
    gamma |= gamma_bit << i

print(gamma * (2 ** length - 1 ^ gamma))
