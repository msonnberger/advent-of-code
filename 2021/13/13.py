from aocd import data

points, folds = data.split('\n\n')
points = [line.split(',') for line in points.splitlines()]
points = [(int(x), int(y)) for x, y in points]
folds = [line.split()[-1].split('=') for line in folds.splitlines()]
folds = [[axis, int(val)] for axis, val in folds]
paper = set()

for point in points:
    paper.add(point)


def part1():
    axis, val = folds[0]
    fold(axis, val)
    print(f"part 1: {len(paper)}")

def part2():
    for axis, val in folds:
        fold(axis, val)

    max_row = max(x for x, _ in paper)
    min_row = min(x for x, _ in paper)
    max_col = max(y for _, y in paper)
    min_col = min(y for _, y in paper)

    print("part 2:")
    for y in range(min_col, max_col + 1):
        line = ""
        for x in range(min_row, max_row + 1):
            line += "#" if (x, y) in paper else " "
        
        print(line)

def fold(axis, val):
    global paper
    folded = set()

    for x, y in paper:
        if axis == 'x' and x > val:
            folded.add((2 * val - x, y))
        elif axis == 'y' and y > val:
            folded.add((x, 2 * val - y))
        else:
            folded.add((x, y))

    paper = folded

part1()
part2()