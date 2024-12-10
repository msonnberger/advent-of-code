from aocd import data
from collections import defaultdict
from itertools import combinations

n, m = len(data.splitlines()), len(data.splitlines()[0])
frequencies = defaultdict(list)
antinodes = set()
antinodes2 = set()

for i, line in enumerate(data.splitlines()):
    for j, char in enumerate(line):
        if char != ".":
            frequencies[char].append(complex(i, j))

in_grid = lambda x: 0 <= x.real < n and 0 <= x.imag < m

for freq, nodes in frequencies.items():
    for a, b in combinations(nodes, 2):
        diff = a - b

        if in_grid(a + diff):
            antinodes.add(a + diff)
        if in_grid(b - diff):
            antinodes.add(b - diff)

        antinodes2.update([a, b])
        while in_grid(a + diff):
            antinodes2.add(a + diff)
            a += diff

        while in_grid(b - diff):
            antinodes2.add(b - diff)
            b -= diff


print(f"part 1: {len(antinodes)}")
print(f"part 2: {len(antinodes2)}")
