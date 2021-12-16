#!/usr/bin/env python3

from math import prod

def cut(code, length):
    return code[:length], code[length:]

def parse(code):
    _, code = cut(code, 3)

    code_type, code = cut(code, 3)
    code_type = int(code_type, 2)
    if code_type == 4:
        # literal
        literal = ''
        while len(code) >= 5:
            group, code = cut(code, 5)
            lead, val = cut(group, 1)
            literal += val
            if lead == '0':
                break
        return int(literal, 2), code

    # operator
    length_type, code = cut(code, 1)
    sub_vals = []
    if length_type == '0':
        length, code = cut(code, 15)
        length = int(length, 2)
        sub, code = cut(code, length)
        while len(sub) > 0 and int(sub, 2):
            sub_val, sub = parse(sub)
            sub_vals.append(sub_val)
    else:
        length, code = cut(code, 11)
        length = int(length, 2)
        for _ in range(length):
            sub_val, code = parse(code)
            sub_vals.append(sub_val)

    if code_type == 0:
        # Sum
        return sum(sub_vals), code

    if code_type == 1:
        # Product
        return prod(sub_vals), code

    if code_type == 2:
        # Minimum
        return min(sub_vals), code

    if code_type == 3:
        # Maximum
        return max(sub_vals), code

    if code_type == 5:
        # Greater than
        return 1 if sub_vals[0] > sub_vals[1] else 0, code

    if code_type == 6:
        # Less than
        return 1 if sub_vals[0] < sub_vals[1] else 0, code

    if code_type == 7:
        # Equal
        return 1 if sub_vals[0] == sub_vals[1] else 0, code

with open("input.txt", "r") as f:
    hex_code = f.readline().rstrip()
    code = bin(int(hex_code, 16))[2:].zfill(4 * len(hex_code))

val, _ = parse(code)
print(val)
