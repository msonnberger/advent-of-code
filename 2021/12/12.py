from aocd import lines
from collections import defaultdict

lines = [line.split('-') for line in lines]

def solve():
    graph = defaultdict(list)

    for start, end in lines:
        graph[start].append(end)
        graph[end].append(start)

    print(BFS(graph, 'start', set(), False))

def BFS(graph, node, vis, second_use):
    if node.islower():
        vis = vis | {node}

    if node == 'end':
        return 1

    count = 0

    for neighbor in graph[node]:
        if neighbor == 'start':
            continue

        if neighbor.islower():
            if neighbor in vis:
                if not second_use:
                    count += BFS(graph, neighbor, vis, True)
            else:
                count += BFS(graph, neighbor, vis, second_use)
        else:
            count += BFS(graph, neighbor, vis, second_use)

    return count
    

solve()
