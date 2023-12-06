from aocd import data
import math

lines = data.splitlines()

times = lines[0].split()[1:]
times.append("".join(times))
times = list(map(int, times))

distances = lines[1].split()[1:]
distances.append("".join(distances))
distances = list(map(int, distances))

totals = [0] * len(times)

for t, d, i in zip(times, distances, range(len(times))):
    det = math.sqrt(t**2 - 4 * d)
    x1 = math.ceil((-t + det) / -2)
    x2 = math.floor((-t - det) / -2)
    totals[i] = x2 - x1 + 1

print(f"part 1: {math.prod(totals[:-1])}")
print(f"part 2: {totals[-1]}")
