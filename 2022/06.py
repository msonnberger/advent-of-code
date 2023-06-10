from aocd import data


def find_marker(n):
    for i in range(n, len(data)):
        if len(set(data[i - n : i])) == n:
            return i


print(f"part 1: {find_marker(4)}")
print(f"part 2: {find_marker(14)}")
