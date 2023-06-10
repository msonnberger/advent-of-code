from aocd import lines
from collections import defaultdict

# lines = ["498,4 -> 498,6 -> 496,6", "503,4 -> 502,4 -> 502,9 -> 494,9"]
grid = {}
sign = lambda x: x > 0 - x < 0

for line in lines:
    prev = None
    for pair in line.split(" -> "):
        x, y = map(int, pair.split(","))

        if prev is not None:
            dx = x - prev[0]
            dy = y - prev[1]
            start_x = prev[0] if sign(dx) else x
            end_x = x if sign(dx) else prev[0]
            start_y = prev[1] if sign(dy) else y
            end_y = y if sign(dy) else prev[1]

            for new_x in range(start_x, end_x + 1):
                for new_y in range(start_y, end_y + 1):
                    grid[complex(new_x, new_y)] = "#"

        prev = (x, y)

abyss = max(c.imag for c in grid.keys()) + 1

while 500 not in grid:
    sand = 500 + 0j

    while True:
        if sand.imag >= abyss:
            break
        if sand + 1j not in grid:
            sand += 1j
            continue
        if sand + 1j - 1 not in grid:
            sand += 1j - 1
            continue
        if sand + 1j + 1 not in grid:
            sand += 1j + 1
            continue
        break

    grid[sand] = "o"

print(sum(1 for v in grid.values() if v == "o"))
