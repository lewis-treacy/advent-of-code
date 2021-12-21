#!/usr/bin/env python3

from itertools import product
from collections import defaultdict, Counter

WIN = 21

def mod10(x):
    return ((x-1)%10)+1

with open("input.txt", "r") as f:
    positions = [int(l.rstrip().split()[-1]) for l in f]

rolls = Counter(map(sum, product([1,2,3], repeat=3)))

states = defaultdict(int)
states[tuple(zip(positions, [0,0]))] = 1
wins = [0,0]

while len(states) > 0:
    new_states = defaultdict(int)
    for ((p1, s1), (p2, s2)), count in states.items():
        for roll1 in rolls:
            new_p1 = mod10(p1 + roll1)
            new_s1 = s1 + new_p1
            if new_s1 >= WIN:
                wins[0] += count * rolls[roll1]
                continue
            for roll2 in rolls:
                new_p2 = mod10(p2 + roll2)
                new_s2 = s2 + new_p2
                if new_s2 >= WIN:
                    wins[1] += count * rolls[roll1] * rolls[roll2]
                    continue
                new_states[((new_p1, new_s1), (new_p2, new_s2))] += count * rolls[roll1] * rolls[roll2]
    states = new_states

print(max(wins))
