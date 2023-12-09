from aocd import data

lines = [[int(x) for x in line.split()] for line in data.splitlines()]


def extrapolate(line):
    if not any(line):
        return 0

    diff = [b - a for a, b in zip(line, line[1:])]

    return line[-1] + extrapolate(diff)


print(f"part 1: {sum(extrapolate(line) for line in lines)}")
print(f"part 2: {sum(extrapolate(list(reversed(line))) for line in lines)}")
