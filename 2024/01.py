from aocd import data
from collections import Counter

left, right = [], []

for line in data.splitlines():
    l, r = line.split()
    left.append(int(l))
    right.append(int(r))

total_dist = sum(abs(l - r) for l, r in zip(sorted(left), sorted(right)))

counter = Counter(right)
sim_score = sum(l * counter[l] for l in left)

print(f"part 1: {total_dist}")
print(f"part 2: {sim_score}")