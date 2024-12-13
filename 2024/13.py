from aocd import data
import re

regex = re.compile(r"X(?:\+|=)(\d+), Y(?:\+|=)(\d+)")
total = 0
total2 = 0


def solve(ax, bx, ay, by, px, py):
    b = (px * ay - py * ax) // (ay * bx - by * ax)
    a = (px * by - py * bx) // (by * ax - bx * ay)

    if ax * a + bx * b == px and ay * a + by * b == py:
        return 3 * a + b

    return 0


for block in data.split("\n\n"):
    lines = block.splitlines()
    ax, ay = map(int, regex.search(lines[0]).groups())
    bx, by = map(int, regex.search(lines[1]).groups())
    prize_x, prize_y = map(int, regex.search(lines[2]).groups())

    total += solve(ax, bx, ay, by, prize_x, prize_y)
    total2 += solve(ax, bx, ay, by, prize_x + 10000000000000, prize_y + 10000000000000)

print(f"part 1: {total}")
print(f"part 2: {total2}")
