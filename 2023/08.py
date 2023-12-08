from aocd import data
import math

lines = data.splitlines()
instr = lines[0]
maps = {}

for line in lines[2:]:
    _from, to = line.split(" = ")
    l, r = to.split(", ")
    maps[_from] = (l[1:], r[:-1])

nodes = [node for node in maps if node[-1] == "A"]
index_AAA = nodes.index("AAA")
steps = [0] * len(nodes)
i = 0

while not all(steps):
    for j in range(len(nodes)):
        if steps[j] == 0:
            l, r = maps[nodes[j]]
            ins = instr[i % len(instr)]
            nodes[j] = l if ins == "L" else r

            if nodes[j][-1] == "Z":
                steps[j] = i + 1

    i += 1

print(f"part 1: {steps[index_AAA]}")
print(f"part 2: {math.lcm(*steps)}")
