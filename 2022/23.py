from aocd import lines
from collections import defaultdict


grid = defaultdict(lambda: ".")

for y, line in enumerate(lines):
    for x, c in enumerate(line):
        grid[complex(x, y)] = c

dirs = {
    "N": -1j,
    "NE": 1 - 1j,
    "E": 1,
    "SE": 1 + 1j,
    "S": 1j,
    "SW": -1 + 1j,
    "W": -1,
    "NW": -1 - 1j,
}

prop_order = ["N", "S", "W", "E"]
dir_order = [["N", "NE", "NW"], ["S", "SE", "SW"], ["W", "SW", "NW"], ["E", "SE", "NE"]]


def adj_are_empty(p, di):
    global grid, dirs

    return not any([grid.get(p + dirs[d], 0) == "#" for d in di])


i = 0
while True:
    proposals = {}

    for p in grid:
        if grid[p] != "#":
            continue
        if adj_are_empty(p, dirs.keys()):
            continue

        for j in range(4):
            if adj_are_empty(p, dir_order[(j + i) % 4]):
                k = p + dirs[prop_order[(j + i) % 4]]

                if k in proposals:
                    del proposals[k]
                else:
                    proposals[k] = p

                break

    for prop, orig in proposals.items():
        grid[prop] = "#"
        grid[orig] = "."

    i += 1

    if not proposals:
        print(f"part 2: {i}")
        exit(0)

    if i == 10:
        minx = int(min([p.real for p in grid if grid[p] == "#"]))
        miny = int(min([p.imag for p in grid if grid[p] == "#"]))
        maxx = int(max([p.real for p in grid if grid[p] == "#"]))
        maxy = int(max([p.imag for p in grid if grid[p] == "#"]))

        count = 0
        for x in range(minx, maxx + 1):
            for y in range(miny, maxy + 1):
                if grid[complex(x, y)] == ".":
                    count += 1

        print(f"part 1: {count}")
