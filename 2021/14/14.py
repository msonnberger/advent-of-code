from aocd import data
from collections import defaultdict

template, rules = data.split("\n\n")
rules_list = [rule.split(" -> ") for rule in rules.splitlines()]
rules = {}

for a, b in rules_list:
    rules[a] = b


def solve(steps):
    pair_counts = defaultdict(int)
    for i in range(len(template) - 1):
        pair_counts[template[i:i+2]] += 1

    for _ in range(steps):
        new_counters = defaultdict(int)

        for pair, count in pair_counts.items():
            insert = rules[pair]
            new_counters[pair[0] + insert] += count
            new_counters[insert + pair[1]] += count

        pair_counts = new_counters
            
    letter_counts = defaultdict(int)

    for pair, count in pair_counts.items():
        letter_counts[pair[0]] += count

    letter_counts[template[-1]] += 1

    max_count = max(letter_counts.values())
    min_count = min(letter_counts.values())

    return max_count - min_count

print(f"part 1: {solve(10)}")
print(f"part 2: {solve(40)}")
