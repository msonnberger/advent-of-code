from aocd import lines
from collections import defaultdict
from priority_queue import PriorityQueue
import numpy as np

row_count = len(lines)
col_count = len(lines[0])
cave = np.ndarray((row_count, col_count), dtype=int)

for i in range(len(lines)):
    for j in range(len(lines[0])):
        cave[i, j] = int(lines[i][j])

def part1():
    w, h = cave.shape
    goal = (w - 1, h - 1)
    return dijkstra(cave, (0, 0), goal)

def part2():
    global cave
    zero = cave
    one = zero % 9 + 1
    two = one % 9 + 1
    three = two % 9 + 1
    four = three % 9 + 1
    five = four % 9 + 1
    six = five % 9 + 1
    seven = six % 9 + 1
    eight = seven % 9 + 1

    row1 = np.concatenate((zero, one, two, three, four), axis=1)
    row2 = np.concatenate((one, two, three, four, five), axis=1)
    row3 = np.concatenate((two, three, four, five, six), axis=1)
    row4 = np.concatenate((three, four, five, six, seven), axis=1)
    row5 = np.concatenate((four, five, six, seven, eight), axis=1)

    cave = np.vstack((row1, row2, row3, row4, row5))
    w, h = cave.shape
    goal = (w - 1, h - 1)

    return dijkstra(cave, (0, 0), goal)


def dijkstra(graph, start, goal):
    pq = PriorityQueue()
    dist = defaultdict(lambda: float('inf'))
    prev = defaultdict(lambda: None)

    dist[start] = 0
    
    for r, c in np.ndindex(graph.shape):
        pq.add_task((r, c), dist[r, c])

    while pq:
        curr = pq.pop_task()

        if curr == goal:
            return dist[curr]

        for neighbor in get_neighbors(graph, curr):
            if neighbor in pq:
                x, y = neighbor
                new_dist = dist[curr] + graph[x, y]
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    prev[neighbor] = curr
                    pq.remove_task(neighbor)
                    pq.add_task(neighbor, new_dist)


def get_neighbors(graph, node):
    neighbors = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    out = []
    h, w = graph.shape
    x, y = node

    for dx, dy in neighbors:
        if 0 <= x + dx < h and 0 <= y + dy < w:
            out.append((x + dx, y + dy))

    return out


print(f"part 1: {part1()}")
print(f"part 2: {part2()}")