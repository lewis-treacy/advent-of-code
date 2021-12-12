#!/usr/bin/env python3

def count_paths(graph, path):
    count = 0
    avaliable = [x for x in graph[path[-1]] if x.isupper() or x not in path]
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
        graph[a].add(b)
        graph[b].add(a)

count = count_paths(graph, ['start'])
print(count)
