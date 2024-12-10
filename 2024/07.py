from aocd import data
from operator import mul, add

concat = lambda x, y: int(str(x) + str(y))
total = 0
total2 = 0

for line in data.splitlines():
    l, r = line.split(": ")
    target = int(l)
    nums = list(map(int, r.split()))

    results = [nums[0]]
    results2 = [nums[0]]
    for y in nums[1:]:
        results = [op(x, y) for x in results for op in [add, mul]]
        results2 = [op(x, y) for x in results2 for op in [add, mul, concat]]

    if target in results:
        total += target

    if target in results2:
        total2 += target


print(f"part 1: {total}")
print(f"part 2: {total2}")
