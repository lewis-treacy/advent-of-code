#!/usr/bin/env python3

# This is very messy, didn't enjoy this one too much

from collections import defaultdict
import re
import heapq
import math

COST = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
LETTER_TO_ROOM = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
ROOMS = [2, 4, 6, 8]

def swap(state, hall_pos, room_idx, room_depth):
    rooms, hall = state

    rooms_ = tuple(tuple(hall[hall_pos] if i == room_idx and j == room_depth else x for j, x in enumerate(room)) for i, room in enumerate(rooms))
    hall_ = tuple(rooms[room_idx][room_depth] if i == hall_pos else x for i, x in enumerate(hall))
    return tuple([rooms_, hall_])

def move_room_to_hall(state, room_idx, right, depth=0):
    new_states = []
    rooms, hall = state
    letter = rooms[room_idx][depth]
    room_pos = ROOMS[room_idx]
    hall_range = range(room_pos+1, len(hall)) if right else range(room_pos-1, -1, -1)
    for hall_pos in hall_range:
        if hall[hall_pos] != '':
            break

        if hall_pos in ROOMS:
            continue

        new_state = swap(state, hall_pos, room_idx, depth)
        cost = (abs(hall_pos-ROOMS[room_idx]) + depth + 1) * COST[letter]

        new_states.append((cost, new_state))

    return new_states

def move_hall_to_room(state, hall_pos):
    rooms, hall = state
    letter = hall[hall_pos]
    room_idx = LETTER_TO_ROOM[letter]
    room_pos = ROOMS[room_idx]

    if any(map(lambda x: x != letter and x != '', rooms[room_idx])):
        # Room is occupied by another letter
        return

    # Check the route is clear
    hall_range = range(hall_pos + 1, room_pos) if hall_pos < room_pos else range(room_pos+1, hall_pos)
    for i in hall_range:
        if hall[i] != '':
            return

    depth = len(rooms[room_idx]) - sum(map(lambda x: x == letter, rooms[room_idx])) - 1

    new_state = swap(state, hall_pos, room_idx, depth)
    cost = (abs(hall_pos - room_pos) + 1 + depth) * COST[letter]

    return (cost, new_state)

def get_moves(state):
    new_states = []
    rooms, hall = state

    # Try and move things out of rooms
    for i, room in enumerate(rooms):
        if all(map(lambda x: x != '' and LETTER_TO_ROOM[x] == i, room)):
            continue

        for d in range(len(room)):
            letter = room[d]
            if letter != '':
                # Don't move correct letters
                if LETTER_TO_ROOM[letter] == i and all(map(lambda x: x == letter, room[d+1:])):
                    break

                # Look right
                new_states += move_room_to_hall(state, i, True, d)
                # Look left
                new_states += move_room_to_hall(state, i, False, d)
                break

    # Try moving things into rooms
    for i, l in enumerate(hall):
        if l == '':
            continue

        move = move_hall_to_room(state, i)
        if move:
            new_states.append(move)

    return new_states

def is_success(state):
    rooms, hall = state
    if any(map(lambda x: x != '', hall)):
        return False

    for l, i in LETTER_TO_ROOM.items():
        if any(map(lambda x: x != l, rooms[i])):
            return False

    return True

rooms = [[] for _ in range(4)]
insert = [['D', 'C', 'B', 'A'], ['D', 'B', 'A', 'C']]
with open("input.txt", "r") as f:
    lines = f.readlines()
    for j, m in enumerate(re.finditer(r'([A-Z])', lines[2])):
        rooms[j].append(m.group(1))
    for r in insert:
        for i, c in enumerate(r):
            rooms[i].append(c)
    for j, m in enumerate(re.finditer(r'([A-Z])', lines[3])):
        rooms[j].append(m.group(1))

for i, r in enumerate(rooms):
    rooms[i] = tuple(r)
rooms = tuple(rooms)

start = (rooms, ['']*11)
heap = [(0, start)]
distances = defaultdict(lambda: math.inf)
min_dist = math.inf

while heap:
    dist, state = heapq.heappop(heap)
    moves = get_moves(state)
    for c, s in moves:
        new_dist = dist + c
        if is_success(s) and new_dist < min_dist:
            min_dist = new_dist
        if new_dist < distances[s]:
            distances[s] = new_dist
            heapq.heappush(heap, (new_dist, s))

print(min_dist)
