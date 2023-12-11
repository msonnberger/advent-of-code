from aocd import data
from itertools import combinations


rows = data.splitlines()
no_galaxy_colums = []
no_galaxy_rows = []

for i, row in enumerate(rows):
    if "#" not in row:
        no_galaxy_rows.append(i)

for i, column in enumerate(zip(*rows)):
    if "#" not in column:
        no_galaxy_colums.append(i)


def get_galaxies(expansion_factor):
    galaxies = []
    row_expansion = 0
    col_expansion = 0
    for i in range(len(rows)):
        if i in no_galaxy_rows:
            row_expansion += expansion_factor - 1

        col_expansion = 0

        for j, ch in enumerate(rows[i]):
            if j in no_galaxy_colums:
                col_expansion += expansion_factor - 1
            if ch == "#":
                galaxies.append((i + row_expansion, j + col_expansion))

    return galaxies


pairs1 = combinations(get_galaxies(2), 2)
pairs2 = combinations(get_galaxies(1_000_000), 2)
dist1 = [abs(a[0] - b[0]) + abs(a[1] - b[1]) for a, b in pairs1]
dist2 = [abs(a[0] - b[0]) + abs(a[1] - b[1]) for a, b in pairs2]

print(f"part 1: {sum(dist1)}")
print(f"part 2: {sum(dist2)}")
