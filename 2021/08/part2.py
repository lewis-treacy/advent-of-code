#!/usr/bin/env python3

'''
  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg

len 5: 2, 3, 5
len 6: 0, 6, 9
'''

total = 0
with open("input.txt", "r") as f:
    for line in f:
        a, b = line.split('|')
        a = [set(x) for x in a.split()]
        b = [set(x) for x in b.split()]

        digits = [{}]*10
        lengthFiveCodes = []
        lengthSixCodes = []

        for code in a:
            length = len(code)
            if length == 2:
                digits[1] = code
            elif length == 3:
                digits[7] = code
            elif length == 4:
                digits[4] = code
            elif length == 5:
                lengthFiveCodes.append(code)
            elif length == 6:
                lengthSixCodes.append(code)
            elif length == 7:
                digits[8] = code

        for code in lengthSixCodes:
            if code.issuperset(digits[4]):
                digits[9] = code
            elif code.issuperset(digits[1]):
                digits[0] = code
            else:
                digits[6] = code

        for code in lengthFiveCodes:
            if code.issuperset(digits[7]):
                digits[3] = code
            elif code.issubset(digits[6]):
                digits[5] = code
            else:
                digits[2] = code

        output = ""
        for code in b:
            for i in range(len(digits)):
                if digits[i] == code:
                    output += str(i)
                    break
        total += int(output)

print(total)
