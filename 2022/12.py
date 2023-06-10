from aocd import lines
from collections import deque


values = {}
start = end = None

for i, line in enumerate(lines):
    for j, ch in enumerate(line):
        key = complex(i, j)
        if ch == "S":
            start = key
            values[key] = ord("a")
        elif ch == "E":
            end = key
            values[key] = ord("z")
        else:
            values[key] = ord(ch)


def valid_neighbor(node, neighbor, reverse):
    if reverse:
        return values[node] - 1 <= values.get(neighbor, float("-inf"))
    else:
        return values.get(neighbor, float("inf")) <= values[node] + 1


def bfs(start, goal, reverse=False):
    visited = set()
    queue = deque([[start]])

    if start == goal or chr(values[start]) == goal:
        return 0

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node not in visited:
            visited.add(node)

            for d in [1, -1, 1j, -1j]:
                neighbor = node + d

                if valid_neighbor(node, neighbor, reverse):
                    new_path = path.copy()
                    new_path.append(neighbor)
                    queue.append(new_path)

                    if neighbor == goal or chr(values[neighbor]) == goal:
                        return len(new_path) - 1


print(f"part 1: {bfs(start, end)}")
print(f"part 2: {bfs(end, 'a', reverse=True)}")
