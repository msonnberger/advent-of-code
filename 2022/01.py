from aocd import data

elves = [list(map(int, elf.split())) for elf in data.split("\n\n")]
sums_sorted = sorted([sum(elf) for elf in elves], reverse=True)

print(f"part 1: {sums_sorted[0]}")
print(f"part 2: {sum(sums_sorted[:3])}")
