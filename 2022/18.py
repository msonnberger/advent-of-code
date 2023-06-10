from aocd import lines
from ast import literal_eval
from collections import deque


dirs = [(0, 0, 1), (0, 1, 0), (1, 0, 0), (0, 0, -1), (0, -1, 0), (-1, 0, 0)]

# Part 1

grid = set()
sides = 0

for line in lines:
    grid.add(literal_eval(f"({line})"))

for x, y, z in grid:
    sides += sum([1 for dx, dy, dz in dirs if (x + dx, y + dy, z + dz) not in grid])


# Part 2

xmin = min([x for x, _, _ in grid]) - 1
xmax = max([x for x, _, _ in grid]) + 1
ymin = min([y for _, y, _ in grid]) - 1
ymax = max([y for _, y, _ in grid]) + 1
zmin = min([z for _, _, z in grid]) - 1
zmax = max([z for _, _, z in grid]) + 1

seen = set()
queue = deque()
queue.append((xmin, ymin, zmin))
sides2 = 0

while queue:
    x, y, z = queue.pop()

    if (x, y, z) not in seen:
        seen.add((x, y, z))

        for dx, dy, dz in dirs:
            newx, newy, newz = x + dx, y + dy, z + dz

            if (newx, newy, newz) in grid:
                sides2 += 1

            if (
                xmin <= newx <= xmax
                and ymin <= newy <= ymax
                and zmin <= newz <= zmax
                and (newx, newy, newz) not in grid
            ):
                queue.append((newx, newy, newz))


print(f"part 1: {sides}")
print(f"part 2: {sides2}")
