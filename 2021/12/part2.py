#!/usr/bin/env python3

def get_next_steps(graph, path):
    avaliable = graph[path[-1]]
    visited_twice = any(x.islower() and path.count(x) == 2 for x in path)
    if visited_twice:
        avaliable = [x for x in avaliable if x.isupper() or x not in path]
    return avaliable

def count_paths(graph, path):
    count = 0
    avaliable = get_next_steps(graph, path)
    for a in avaliable:
        new_path = path + [a]
        if a == 'end':
            count += 1
            continue
        count += count_paths(graph, new_path)
    return count

graph = {}
with open("input.txt", "r") as f:
    for l in f:
        a, b = l.rstrip().split('-')
        if a not in graph:
            graph[a] = set()
        if b not in graph:
            graph[b] = set()
        if b != 'start':
            graph[a].add(b)
        if a != 'start':
            graph[b].add(a)

count = count_paths(graph, ['start'])
print(count)
