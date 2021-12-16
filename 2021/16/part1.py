#!/usr/bin/env python3

def cut(code, length):
    return code[:length], code[length:]

def parse(code):
    ver_sum = 0

    version, code = cut(code, 3)
    ver_sum += int(version, 2)

    code_type, code = cut(code, 3)
    code_type = int(code_type, 2)
    if code_type == 4:
        # literal
        while len(code) >= 5:
            group, code = cut(code, 5)
            lead = group[0]
            if lead == '0':
                break
        return ver_sum, code

    # operator
    length_type, code = cut(code, 1)
    if length_type == '0':
        length, code = cut(code, 15)
        length = int(length, 2)
        sub, code = cut(code, length)
        while len(sub) > 0 and int(sub, 2):
            sub_ver_sum, sub = parse(sub)
            ver_sum += sub_ver_sum
    else:
        length, code = cut(code, 11)
        length = int(length, 2)
        for _ in range(length):
            sub_ver_sum, code = parse(code)
            ver_sum += sub_ver_sum

    return ver_sum, code

with open("input.txt", "r") as f:
    hex_code = f.readline().rstrip()
    code = bin(int(hex_code, 16))[2:].zfill(4 * len(hex_code))

ver_sum, _ = parse(code)
print(ver_sum)
