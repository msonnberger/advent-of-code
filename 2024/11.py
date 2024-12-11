from aocd import data
from collections import Counter

stones = Counter(map(int, data.split()))


def blink():
    for stone, count in stones.copy().items():
        if stone == 0:
            stones[1] += count
        elif len(str(stone)) % 2 == 0:
            l, r = (
                str(stone)[: len(str(stone)) // 2],
                str(stone)[len(str(stone)) // 2 :],
            )
            stones[int(l)] += count
            stones[int(r)] += count
        else:
            stones[stone * 2024] += count

        stones[stone] -= count


for i in range(25):
    blink()

print(f"part 1: {stones.total()}")

for i in range(50):
    blink()

print(f"part 2: {stones.total()}")
