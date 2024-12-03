from aocd import data
import re

total1 = total2 = 0
enabled = True

for a, b, do, dont in re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", data):
    if do:
        enabled = True
    elif dont:
        enabled = False
    elif a and b:
        total1 += int(a) * int(b)

        if enabled:
            total2 += int(a) * int(b)


print(f"part 1: {total1}")
print(f"part 2: {total2}")
