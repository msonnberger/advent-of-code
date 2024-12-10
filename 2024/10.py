from aocd import data
from collections import defaultdict


grid = defaultdict(lambda: -1)
trailheads = []
for i, line in enumerate(data.splitlines()):
    for j, char in enumerate(line):
        grid[complex(i, j)] = int(char)

        if int(char) == 0:
            trailheads.append(complex(i, j))


def score(pos, part2=False):
    seen = set()

    def dfs(pos):
        if not part2 and pos in seen:
            return 0

        seen.add(pos)

        if grid[pos] == 9:
            return 1

        return sum(
            dfs(pos + d) for d in [1, -1, 1j, -1j] if grid[pos + d] == grid[pos] + 1
        )

    return dfs(pos)


print(f"part 1: {sum(score(t) for t in trailheads)}")
print(f"part 2: {sum(score(t, part2=True) for t in trailheads)}")
