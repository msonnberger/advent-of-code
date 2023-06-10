from aocd import lines

row_len = len(lines)
col_len = len(lines[0])
sea = dict()

for r in range(row_len):
    for c in range(col_len):
        sea[r, c] = lines[r][c]

def solve():
    moved = True
    count = 0
    while moved:
        moved = step()
        count += 1

    print("part 1:", count)

def step():
    move_right = set()

    for coords, val in sea.items():
        if val == '>':
            r, c = coords
            right = r, (c + 1) % col_len
            if sea[right] == '.':
                move_right.add((coords, right))

    for coords, right in move_right:
        sea[coords] = '.'
        sea[right] = '>'

    move_down = set()

    for coords, val in sea.items():
        if val == 'v':
            r, c = coords
            down = (r + 1) % row_len, c
            if sea[down] == '.':
                move_down.add((coords, down))

    for coords, down in move_down:
        sea[coords] = '.'
        sea[down] = 'v'

    return len(move_down) + len(move_right) > 0


solve()