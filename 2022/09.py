from aocd import lines

knots = [0j] * 10
visited_first = set()
visited_last = set()

directions = {"R": 1, "L": -1, "U": 1j, "D": -1j}

sign = lambda z: ((z.real > 0) - (z.real < 0)) + ((z.imag > 0) - (z.imag < 0)) * 1j


for line in lines:
    direction, length = line.split()
    length = int(length)

    for _ in range(length):
        knots[0] += directions[direction]

        for i in range(1, len(knots)):
            d = knots[i - 1] - knots[i]

            if abs(d) >= 2:
                knots[i] += sign(d)

            if i == 1:
                visited_first.add(knots[i])

            if i == len(knots) - 1:
                visited_last.add(knots[i])


print(f"part 1: {len(visited_first)}")
print(f"part 2: {len(visited_last)}")
