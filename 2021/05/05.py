import re
from aocd import lines
from collections import Counter

#lines = open("example.txt").read().splitlines()

def solve(diagonal = True):
    pattern = re.compile("(\d+),(\d+) -> (\d+),(\d+)")
    counter = Counter()

    for line in lines:
        match = pattern.match(line)
        x1, y1, x2, y2 = [int(x) for x in match.groups()]

        if x1 == x2:
            dx = 0
        elif x2 > x1:
            dx = 1
        else:
            dx = -1
        
        if y1 == y2:
            dy = 0
        elif y2 > y1:
            dy = 1
        else:
            dy = -1
        
        if not diagonal and dx != 0 and dy != 0:
            continue

        counter[(x1,y1)] += 1

        while x1 != x2 or y1 != y2:
            x1 += dx
            y1 += dy
            counter[(x1,y1)] += 1

    result = sum(val >= 2 for val in counter.values())
    part = 2 if diagonal else 1
    print(f'part {part}: {result}')

solve(diagonal=False)
solve()