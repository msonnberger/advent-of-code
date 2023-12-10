from aocd import data
from collections import defaultdict, deque

lines = data.splitlines()
graph = defaultdict(list)
start = None

for y, line in enumerate(lines):
    for x, sym in enumerate(line):
        neighbors = []
        pos = complex(x, y)
        match sym:
            case "|":
                neighbors = [-1j, +1j]
            case "-":
                neighbors = [-1, +1]
            case "L":
                neighbors = [-1j, +1]
            case "J":
                neighbors = [-1j, -1]
            case "7":
                neighbors = [1j, -1]
            case "F":
                neighbors = [1, 1j]
            case "S":
                start = pos

        for n in neighbors:
            if 0 <= (pos + n).real < len(lines) and 0 <= (pos + n).imag < len(line):
                graph[pos].append(pos + n)

start_neighbors = []

for node, neighbors in graph.items():
    for neighbor in neighbors:
        if neighbor == start:
            start_neighbors.append(node)

graph[start] = start_neighbors


def bfs(graph, node):
    queue = deque([start])
    visited = set()
    distances = {}
    distances[start] = 0

    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                distances[neighbor] = distances[node] + 1
                queue.append(neighbor)

    return max(distances.values()), visited


max_dist, loop_nodes = bfs(graph, node)
print(f"part 1: {max_dist}")


### PART 2

start_neighbor_diffs = frozenset(start - n for n in start_neighbors)
diff_to_pipe = {
    frozenset([1j, -1j]): "|",
    frozenset([1, -1]): "-",
    frozenset([1j, -1]): "L",
    frozenset([1j, 1]): "J",
    frozenset([-1j, 1]): "7",
    frozenset([-1j, -1]): "F",
}

lines = data.replace("S", diff_to_pipe[start_neighbor_diffs]).splitlines()
inside_count = 0
north_pipes = set(["J", "L", "|"])

for y, line in enumerate(lines):
    north_pipe_count = 0

    for x, sym in enumerate(line):
        if complex(x, y) in loop_nodes and sym in north_pipes:
            north_pipe_count += 1
        elif complex(x, y) not in loop_nodes and north_pipe_count % 2 == 1:
            inside_count += 1

print(f"part 2: {inside_count}")
