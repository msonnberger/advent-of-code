import re
from aocd import lines
from collections import deque
from queue import PriorityQueue

data = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""
lines = data.splitlines()

graph = {}
rates = {}
regex = re.compile(
    r"Valve ([A-Z]+) has flow rate=(\d+); (tunnel|tunnels) (lead|leads) to (valve|valves) (\D+)"
)

for line in lines:
    name, rate, _, _, _, other = regex.match(line).groups()
    neighbors = []
    [neighbors.append(n) for n in other.split(", ")]
    graph[name] = neighbors
    rates[name] = int(rate)


def dijkstra(start):
    queue = PriorityQueue()
    queue.put((-rates[start], start))
    visited = set()

    while queue:
        node = queue.get()
        print(node[1])

        if node not in visited:
            visited.add(node)

            for n in graph[node[1]]:
                queue.put((-rates[n], n))


# dijkstra("AA")
