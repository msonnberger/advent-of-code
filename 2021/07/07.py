from aocd import data
from statistics import median

positions = [int(x) for x in data.split(',')]

def n_sum(n):
    return (n * n + n) // 2

def part2():
    min_cost = 1e12

    for i in range(min(positions), max(positions) + 1):
        total_cost = sum([n_sum(abs(pos - i)) for pos in positions])
        min_cost = min(min_cost, total_cost)

    print(f"part 2: {min_cost}")

def part1():
    result = int(sum([abs(pos - median(positions)) for pos in positions]))
    print(f"part 1: {result}")

part1()
part2()