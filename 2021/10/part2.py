#!/usr/bin/env python3

from statistics import median

close_to_open = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}

open_to_close = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

points = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

def process_line(line):
    stack = []
    for b in line:
        if b in {'(','[','{','<'}:
            stack.append(b)
            continue
        c = stack.pop()
        if close_to_open[b] != c:
            return

    if len(stack) != 0:
        score = 0
        completion = [open_to_close[b] for b in reversed(stack)]
        for c in completion:
            score *= 5
            score += points[c]
        return score

scores = []
with open("input.txt", "r") as f:
    for line in f:
        score = process_line(line.rstrip())
        if score:
            scores.append(score)

print(median(scores))
