from aocd import data
from collections import defaultdict
import math

gear_ratios = 0
part_numbers = 0
grid = defaultdict(lambda: ".")

for y, line in enumerate(data.splitlines()):
    x = 0
    while x < len(line):
        d = x
        while d < len(line) and line[d].isdigit():
            d += 1

        if d > x:
            num = int(line[x:d])

            while d > x:
                grid[complex(x, y)] = num
                x += 1
        else:
            grid[complex(x, y)] = line[x]
            x += 1


dirs = [
    1,
    1 + 1j,
    1j,
    -1 + 1j,
    -1,
    -1 - 1j,
    -1j,
    1 - 1j,
]

for key, value in grid.items():
    c = set()

    if not value == "." and not type(value) == int:
        for d in dirs:
            if type(grid[key + d]) == int:
                c.add(grid[key + d])

    part_numbers += sum(c)
    if value == "*" and len(c) == 2:
        gear_ratios += math.prod(c)

print(f"part 1: {part_numbers}")
print(f"part 2: {gear_ratios}")
