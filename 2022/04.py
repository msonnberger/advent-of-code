from aocd import lines

partial = full = 0

for line in lines:
    l, r = line.split(",")
    l1, l2 = l.split("-")
    r1, r2 = r.split("-")

    lset = set(range(int(l1), int(l2) + 1))
    rset = set(range(int(r1), int(r2) + 1))

    if len(lset & rset) == len(lset) or len(lset & rset) == len(rset):
        full += 1

    if lset & rset:
        partial += 1

print(f"part 1: {full}")
print(f"part 2: {partial}")
