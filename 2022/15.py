from aocd import lines
from collections import defaultdict
from tqdm import tqdm

data = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
"""


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


row = 10
x_max = 4000000
# lines = data.splitlines()
# x_max = 20
occ = set()
beac = set()
distress = set()
occ_rows = defaultdict(list)


def fill_grid(s, d):
    global occ, distress
    l, r = int(s.real - d), int(s.real + d + 1)
    y = int(s.imag)
    i = 0

    while l <= r:
        ran = range(l, r)
        if y + i == row or y - i == row:
            occ |= set(ran)

        if y + i <= x_max:
            occ_rows[y + i].append(set(ran))

        if y - i <= x_max:
            occ_rows[y - i].append(set(ran))

        l += 1
        r -= 1
        i += 1


for i, line in enumerate(tqdm(lines)):
    l, r = line.split(":")
    xs = int(l[l.index("x=") + 2 : l.index(", ")])
    ys = int(l[l.index("y=") + 2 :])
    xb = int(r[r.index("x=") + 2 : r.index(", ")])
    yb = int(r[r.index("y=") + 2 :])

    d = manhattan([xs, ys], [xb, yb])
    fill_grid(complex(xs, ys), d)

    if (yb) == row:
        beac.add(xb)


print(len(occ - beac))


def missing_elements(L):
    start, end = L[0], L[-1]
    return sorted(set(range(start, end + 1)).difference(L))


for k, v in tqdm(occ_rows.items()):
    inter = list(set.union(*v))
    missing = missing_elements(sorted(inter))
    if len(missing) == 1:
        print(missing[0] * 4000000 + k)
        exit(0)
