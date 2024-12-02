from aocd import data

reports = [list(map(int, line.split())) for line in data.splitlines()]

def is_safe(report):
    deltas = [a - b for a, b in zip(report, report[1:])]
    return all(d in [1, 2, 3] for d in deltas) or all(d in [-1, -2, -3] for d in deltas)


safe1 = sum(is_safe(r) for r in reports)
print(f"part 1: {safe1}")

safe2 = sum(any(is_safe(r[:i] + r[i + 1 :]) for i in range(len(r))) for r in reports)
print(f"part 2: {safe2}")