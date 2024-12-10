from aocd import data

disk = []
files, spaces = [], []
pos = 0
file_id = 0

for i, c in enumerate(data):
    if i % 2 == 0:
        files.append((pos, int(c), file_id))
    else:
        spaces.append((pos, int(c)))

    for _ in range(int(c)):
        pos += 1
        if i % 2 == 0:
            disk.append(file_id)
        else:
            disk.append(".")

    if i % 2 == 0:
        file_id += 1

l, r = 0, len(disk) - 1

while disk[l] != ".":
    l += 1

while disk[r] == ".":
    r -= 1

while l < r:
    disk[l], disk[r] = disk[r], disk[l]

    l += 1
    while disk[l] != ".":
        l += 1

    r -= 1
    while disk[r] == ".":
        r -= 1

checksum = 0

for i in range(len(disk)):
    if disk[i] != ".":
        checksum += i * disk[i]

# Part 2

for f_i, (f_pos, f_size, fid) in enumerate(reversed(files)):
    for s_i, (s_pos, s_size) in enumerate(spaces):
        if s_pos >= f_pos:
            break
        if f_size <= s_size:
            spaces[s_i] = (s_pos + f_size, s_size - f_size)
            files[len(files) - f_i - 1] = (s_pos, f_size, fid)
            break

checksum2 = 0

for pos, size, id in files:
    for i in range(size):
        checksum2 += (pos + i) * id


print(f"part 1: {checksum}")
print(f"part 2: {checksum2}")
