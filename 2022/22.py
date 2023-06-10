from aocd import lines

grid = {}
lines, moves = lines[:-2], lines[-1]

for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c == "." or c == "#":
            grid[complex(j + 1, i + 1)] = c


def calc_next_pos(pos, facing):
    global grid

    if pos + facing in grid:
        return pos + facing

    match facing:
        case -1:
            x, y = (
                max([p.real for p in grid if p.imag == pos.imag]),
                pos.imag,
            )

        case 1:
            x, y = (
                min([p.real for p in grid if p.imag == pos.imag]),
                pos.imag,
            )

        case -1j:
            x, y = pos.real, max([p.imag for p in grid if p.real == pos.real])

        case 1j:
            x, y = pos.real, min([p.imag for p in grid if p.real == pos.real])

    return complex(x, y)


pos = 1 + 1j
facing = 1

ptr = 0
last = 0

while ptr < len(moves):
    while ptr < len(moves) and moves[ptr] not in ["L", "R"]:
        ptr += 1

    steps = int(moves[last:ptr])

    for step in range(steps):
        next_pos = calc_next_pos(pos, facing)
        if grid[next_pos] == "#":
            break

        pos = next_pos

    rot = moves[ptr] if ptr < len(moves) else None

    if rot == "R":
        facing *= 1j
    elif rot == "L":
        facing *= -1j

    ptr += 1
    last = ptr


rot_val = {-1: 2, 1: 0, 1j: 1, -1j: 3}
print(int(pos.imag * 1000 + pos.real * 4 + rot_val[facing]))
