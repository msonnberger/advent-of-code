from aocd import lines
from collections import deque as queue

#lines = ["2199943210","3987894921","9856789892","8767896789","9899965678"]

floor = [[int(x) for x in line] for line in lines]

def solve():
    total = 0
    sizes = []
    for x in range(len(floor)):
        for y in range(len(floor[x])):
            if check_neighbors(x, y):
                total += 1 + floor[x][y]
                sizes.append(basin_size([], x, y))

    print(f"part 1: {total}")
    largest = sorted(sizes)[-3:]
    res = largest[0] * largest[1] * largest[2]
    print(f"part 2: {res}")

def check_neighbors(x, y):
    if x < len(floor) - 1 and floor[x + 1][y] <= floor[x][y]:
        return False
    
    if x > 0 and floor[x - 1][y] <= floor[x][y]:
        return False 

    if y > 0 and floor[x][y - 1] <= floor[x][y]:
        return False

    if y < len(floor[x]) - 1 and floor[x][y + 1] <= floor[x][y]:
        return False

    return True

def basin_size(vis, x, y):
    q = queue()
    q.append((x, y))
    vis.append((x, y))
    size = 1
 
    while (len(q) > 0):
        cell = q.popleft()
        x = cell[0]
        y = cell[1]
        
        if (is_valid(vis, x + 1, y, floor[x][y])):
            q.append((x + 1, y, floor[x][y]))
            vis.append((x + 1, y))
            size += 1

        if (is_valid(vis, x, y + 1, floor[x][y])):
            q.append((x, y + 1))
            vis.append((x, y + 1))
            size += 1

        if (is_valid(vis, x - 1, y, floor[x][y])):
            q.append((x - 1, y))
            vis.append((x - 1, y))
            size += 1

        if (is_valid(vis, x, y - 1, floor[x][y])):
            q.append((x, y - 1))
            vis.append((x, y - 1))
            size += 1

    return size

def is_valid(vis, x, y, prev_val):
    if (x < 0 or y < 0 or x > len(floor) - 1 or y > len(floor[0]) - 1):
        return False
    
    if (x, y) in vis:
        return False
    
    if floor[x][y] == 9:
        return False

    if floor[x][y] < prev_val:
        return False

    return True

solve()