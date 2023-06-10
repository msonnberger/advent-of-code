from aocd import data

# data = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"

rocks = [
    [2, 3, 4, 5],
    [3, 2 + 1j, 3 + 1j, 4 + 1j, 3 + 2j],
    [2, 3, 4, 4 + 1j, 4 + 2j],
    [2, 2 + 1j, 2 + 2j, 2 + 3j],
    [2, 2 + 1j, 3, 3 + 1j],
]

tower = set(range(7))
jet_idx = 0

for rock_idx in range(2022):
    rock = rocks[rock_idx % len(rocks)]
    y_off = max(p.imag for p in tower) + 4
    rock = [p + complex(0, y_off) for p in rock]

    while True:
        jet = data[jet_idx % len(data)]
        if jet == "<":
            dx = -1
        else:
            dx = 1
        jet_idx += 1
        new_rock = [p + dx for p in rock]
        if any(p.real not in range(7) for p in new_rock):
            new_rock = rock
        elif any(p in tower for p in new_rock):
            new_rock = rock
        rock = new_rock
        new_rock = [p - 1j for p in rock]
        if any(p in tower for p in new_rock):
            tower |= set(rock)
            break

        rock = new_rock

print(max(int(p.imag) for p in tower))
