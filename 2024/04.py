from aocd import data
from util import parse_grid

grid, n, m = parse_grid(data)
dirs = [1, 1j, -1, -1j, 1 + 1j, 1 - 1j, -1 + 1j, -1 - 1j]
xmas_count = 0
cross_count = 0

for i in range(n):
    for j in range(m):
        pos = complex(i, j)
        for d in dirs:
            word = grid[pos] + grid[pos + d] + grid[pos + d + d] + grid[pos + d + d + d]

            if word == "XMAS":
                xmas_count += 1

        one = grid[pos + (-1 - 1j)] + grid[pos] + grid[pos + (1 + 1j)]
        two = grid[pos + (-1 + 1j)] + grid[pos] + grid[pos + (1 - 1j)]

        if (one == "MAS" or one == "SAM") and (two == "MAS" or two == "SAM"):
            cross_count += 1

print(f"part 1: {xmas_count}")
print(f"part 2: {cross_count}")
