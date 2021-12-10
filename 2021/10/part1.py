#!/usr/bin/env python3

brackets = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}

points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

def process_line(line):
    stack = []
    for b in line:
        if b in {'(','[','{','<'}:
            stack.append(b)
            continue
        c = stack.pop()
        if brackets[b] != c:
            return points[b]
    return 0


score = 0
with open("input.txt", "r") as f:
    for line in f:
        score += process_line(line.rstrip())

print(score)
