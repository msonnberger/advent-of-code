from aocd import data

grid = {
    complex(j, i): char
    for i, line in enumerate(data.splitlines())
    for j, char in enumerate(line)
}

regions = []
visited = set()

for pos, char in grid.items():
    if pos in visited:
        continue

    region = {pos}
    stack = [pos]

    while stack:
        pos = stack.pop()
        visited.add(pos)

        for neighbor in [pos + 1, pos - 1, pos + 1j, pos - 1j]:
            if neighbor in grid and grid[neighbor] == char and neighbor not in region:
                region.add(neighbor)
                stack.append(neighbor)

    regions.append(region)


perimeter = lambda region: sum(
    neighbor not in region
    for pos in region
    for neighbor in [pos + 1, pos - 1, pos + 1j, pos - 1j]
)


def corners(region):
    corners = 0

    for pos in region:
        if pos - 1 not in region and pos - 1j not in region:
            corners += 1
        if pos + 1 not in region and pos - 1j not in region:
            corners += 1
        if pos + 1 not in region and pos + 1j not in region:
            corners += 1
        if pos - 1 not in region and pos + 1j not in region:
            corners += 1

        if pos - 1 in region and pos - 1j in region and pos - 1 - 1j not in region:
            corners += 1
        if pos + 1 in region and pos - 1j in region and pos + 1 - 1j not in region:
            corners += 1
        if pos + 1 in region and pos + 1j in region and pos + 1 + 1j not in region:
            corners += 1
        if pos - 1 in region and pos + 1j in region and pos - 1 + 1j not in region:
            corners += 1

    return corners


price = sum(len(region) * perimeter(region) for region in regions)
price2 = sum(len(region) * corners(region) for region in regions)

print(f"part 1: {price}")
print(f"part 2: {price2}")
