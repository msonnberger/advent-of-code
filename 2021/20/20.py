from aocd import lines
from collections import defaultdict


algo = lines[0]
lines = lines[2:]
size = len(lines)
orig = defaultdict(lambda:'.')

for i in range(size):
    for j in range(size):
        orig[(i, j)] = lines[i][j]


def enhance(pic, start, end):
    enhanced = defaultdict()
    
    for x in range(start, end):
        for y in range(start, end):
            conv = ''
            for i in (-1, 0, 1):
                for j in (-1, 0, 1):
                    point = (x + i, y + j)
                    conv += pic[point]

            conv = conv.replace('.', '0').replace('#', '1')
            enhanced[(x, y)] = algo[int(conv, 2)]
    
    return enhanced


def solve(n, image):
    start = -1
    end = size + 1

    for i in range(n):
        image.default_factory = (lambda:'.') if i % 2 == 0 else (lambda:'#')
        image = enhance(image, start, end)
        start -= 1
        end += 1

    return sum(val == '#' for val in image.values())


print('part 1:', solve(2, orig))
print('part 2:', solve(50, orig))
