from aocd import lines
import numpy as np

lines = [[c for c in line] for line in lines]

def solve():
    matrix = np.array(lines, int)
    flash_count = 0
    flashed_this_step = 0
    i = 1

    while flashed_this_step != matrix.size:
        has_flashed = np.zeros(matrix.shape)
        matrix += 1

        for x, y in np.ndindex(matrix.shape):
            if matrix[x, y] > 9:
                flash(matrix, x, y, has_flashed)

        matrix = np.where(has_flashed != 0, 0, matrix)
        flashed_this_step = np.count_nonzero(has_flashed)
        flash_count += flashed_this_step

        if i == 100:
            print(f"part 1: {flash_count}")

        i += 1
        
    print(f"part 2: {i - 1}")

def flash(matrix, x, y, has_flashed):
    if matrix[x, y] <= 9:
        return

    if has_flashed[x, y] != 0:
        return
    
    has_flashed[x, y] = 1

    neighbors = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
    h, w = matrix.shape

    for dx, dy in neighbors:
        if 0 <= x + dx < h and 0 <= y + dy < w:
            matrix[x + dx, y + dy] += 1
            flash(matrix, x + dx, y + dy, has_flashed)


solve()