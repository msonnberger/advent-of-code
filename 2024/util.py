def parse_grid(data: str) -> tuple[dict[complex, str], int, int]:
    from collections import defaultdict

    grid = defaultdict(lambda: ".")
    n, m = len(data.splitlines()), len(data.splitlines()[0])
    for i, line in enumerate(data.splitlines()):
        for j, char in enumerate(line):
            grid[complex(i, j)] = char
    return grid, n, m
