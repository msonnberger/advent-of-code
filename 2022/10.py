from aocd import lines
import numpy as np
import math

x = 1
cycle_count = 0
total = 0
crt = np.chararray((6, 40), unicode=True)
crt[:] = "."


def cycle():
    global cycle_count, total

    row = math.ceil(cycle_count // 40)

    if cycle_count - 1 <= x + row * 40 <= cycle_count + 1:
        crt[row][cycle_count - row * 40] = "#"

    cycle_count += 1

    if cycle_count in range(20, 221, 40):
        total += cycle_count * x


for line in lines:
    cycle()

    if line.startswith("addx"):
        cycle()
        x += int(line.split()[1])


print(f"part 1: {total}")
print(f"part 2:")
[print("".join(line)) for line in crt]
