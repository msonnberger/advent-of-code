from aocd import lines
import numpy as np

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
height, width = len(lines), len(lines[0])

grid = np.empty([height, width])

for i, line in enumerate(lines):
    for j, x in enumerate(line):
        grid[i][j] = int(lines[i][j])


def calc(i, j):
    visible = False
    score = 1

    for di, dj in directions:
        direction_score = 0
        new_i, new_j = i + di, j + dj

        while new_i >= 0 and new_i < height and new_j >= 0 and new_j < width:
            direction_score += 1

            if grid[new_i][new_j] >= grid[i][j]:
                break

            new_i += di
            new_j += dj

        if not (new_i >= 0 and new_i < height and new_j >= 0 and new_j < width):
            visible = True

        score *= direction_score

    return (visible, score)


visible_count = 0
max_score = 0

for i in range(height):
    for j in range(width):
        visible, score = calc(i, j)
        if visible:
            visible_count += 1

        max_score = max(max_score, score)

print(f"part 1: {visible_count}")
print(f"part 2: {max_score}")
