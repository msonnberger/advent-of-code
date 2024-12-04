from aocd import data

nice_count = 0
nice_count2 = 0

for line in data.splitlines():
    vowels = sum(c in "aeiou" for c in line)
    double = any(a == b for a, b in zip(line, line[1:]))
    banned = any(s in line for s in ["ab", "cd", "pq", "xy"])
    if vowels >= 3 and double and not banned:
        nice_count += 1

    double = any(line.count(line[i : i + 2]) > 1 for i in range(len(line) - 1))
    repeat = any(a == b for a, b in zip(line, line[2:]))
    if double and repeat:
        nice_count2 += 1

print(f"part 1: {nice_count}")
print(f"part 2: {nice_count2}")
