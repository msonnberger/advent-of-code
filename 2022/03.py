from aocd import lines


def get_prio(c):
    if c.islower():
        return ord(c) - ord("a") + 1
    else:
        return ord(c) - ord("A") + 1 + 26


def part1():
    total = 0

    for line in lines:
        mid = len(line) // 2
        left, right = line[:mid], line[mid:]
        common = set(left) & set(right)
        total += get_prio(common.pop())

    return total


def part2():
    total = 0

    for i in range(0, len(lines), 3):
        group = lines[i : i + 3]
        common = set.intersection(*map(set, group))
        total += get_prio(common.pop())

    return total


print(f"part 1: {part1()}")
print(f"part 2: {part2()}")
