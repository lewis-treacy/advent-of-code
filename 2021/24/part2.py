#!/usr/bin/env python3

# I found the problem very poorly defined, becasue of this I'm not sure if this
# solution is what was intended or even works on other inputs but it works for
# mine

# Each digit input has this function applied to it with z being the only thing
# to pass between them
# w = int(input())
# x = int((z % 26) + b != w)
# z //= a
# z *= 25*x+1
# z += (w+c)*x

# z acts as a stack, using base 26 to encode the numbers pushed to it

# for each digit input
# if a == 1 then a number is pushed
# if a == 26 then a number is popped and pushed
# by making x = 0 we can stop the number from being pushed

# There are 6 pushes and 6 pops so my making x = 0 on every pop we can remove
# everything from the stack, making z = 0

# here is my input analysed:
# index                       0 1 2  3 4  5 6 7  8 9  10 11 12 13
# * = push, / = pop           * * *  * /  * * /  * /  /  /  /  /
# b                                    -7     -5   -3 0  -5 -9 0
# c                           6 7 10 2 15 8 1 10 5 3  5  1  12 10

# with i as an array of the digits input:
# i[pop] = i[push] + c_push + b_pop
# i[4] = i[3] + 2 - 7
# i[7] = i[6] + 1 - 5
# i[9] = i[8] + 5 - 3
# i[10] = i[5] + 8 + 0
# i[11] = i[2] + 10 - 5
# i[12] = i[1] + 7 - 9
# i[13] = i[0] + 6 + 0

import re

def analyse(instructions):
    mapping = {}
    i = -1
    stack = []
    curr = {k: 0 for k in ['a','b','c']}
    for ins in instructions:
        if ins[0] == 'inp':
            if curr['a'] == 1:
                stack.append((i, curr['b'], curr['c']))
            elif curr['a'] == 26:
                old = stack.pop()
                mapping[i] = (old[0], curr['b'] + old[2])
            i += 1
        if ins[0] == 'div' and ins[1] == 'z':
            # extracts a
            curr['a'] = ins[2]
        if ins[0] == 'add' and ins[1] == 'x' and type(ins[2]) == int:
            # extracts b
            curr['b'] = ins[2]
        if ins[0] == 'add' and ins[1] == 'y' and type(ins[2]) == int:
            # extracts c
            curr['c'] = ins[2]
    old = stack.pop()
    mapping[i] = (old[0], curr['b'] + old[2])

    return mapping

with open("input.txt", "r") as f:
    instructions = [[int(p) if re.match(r"^-?[0-9]+$", p) else p for p in l.rstrip().split()] for l in f]

analysis = analyse(instructions)
input = [0]*14
for i in range(len(input)):
    if i in analysis:
        a = analysis[i]
        digit = input[a[0]] + a[1]
        if digit >= 1:
            input[i] = digit
        else:
            diff = 1 - digit
            input[a[0]] += diff
            input[i] = 1
    else:
        input[i] = 1

print("".join(map(str, input)))
