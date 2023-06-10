from aocd import lines
from collections import defaultdict
from itertools import accumulate

cwd = []
sizes = defaultdict(int)

for line in lines:
    words = line.split()

    if words[0] == "$" and words[1] == "cd":
        if words[2] == "/":
            cwd = [""]
        elif words[2] == "..":
            cwd.pop()
        else:
            cwd.append(words[2])
    elif words[0].isnumeric():
        for d in accumulate(cwd):
            sizes[d] += int(words[0])


total = sum([x for x in sizes.values() if x <= 100000])

root_size = sizes[""]
to_remove = min([x for x in sizes.values() if root_size - x <= 40000000])

print(f"part 1: {total}")
print(f"part 2: {to_remove}")
