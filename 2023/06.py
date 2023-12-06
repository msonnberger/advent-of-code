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

for time, distance, i in zip(times, distances, range(len(times))):
    for ms in range(1, time):
        if ms * (time - ms) > distance:
            totals[i] += 1

print(f"part 1: {math.prod(totals[:-1])}")
print(f"part 2: {totals[-1]}")
