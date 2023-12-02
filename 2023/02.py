import re
import math
from collections import defaultdict
from aocd import data

possible_sum = 0
power_sum = 0
available = {"red": 12, "green": 13, "blue": 14}

for line in data.splitlines():
    game_id = int(re.search(r"\d+", line).group())
    game_possible = True
    maximums = defaultdict(int)

    for value, color in re.findall(r"(\d+) (\w+)", line):
        if int(value) > available[color]:
            game_possible = False

        maximums[color] = max(maximums[color], int(value))

    if game_possible:
        possible_sum += game_id

    power_sum += math.prod(maximums.values())


print(f"part 1: {possible_sum}")
print(f"part 2: {power_sum}")
