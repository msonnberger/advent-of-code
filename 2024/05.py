from aocd import data
from functools import cmp_to_key

rules, updates = data.split("\n\n")
rules = [(int(a), int(b)) for a, b in (line.split("|") for line in rules.splitlines())]
updates = [line.split(",") for line in updates.splitlines()]
updates_to_i = [{int(val): i for i, val in enumerate(line)} for line in updates]

total = 0
total2 = 0

for update in updates:
    nums = [int(val) for val in update]
    num_to_i = {val: i for i, val in enumerate(nums)}

    printed = all(
        a not in num_to_i or b not in num_to_i or num_to_i[a] < num_to_i[b]
        for a, b in rules
    )

    if printed:
        total += nums[len(nums) // 2]
    else:
        nums.sort(key=cmp_to_key(lambda a, b: -1 if ((a, b) in rules) else 1))
        total2 += nums[len(nums) // 2]

print(f"part 1: {total}")
print(f"part 2: {total2}")
