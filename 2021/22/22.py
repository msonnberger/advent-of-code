from aocd import lines
from collections import defaultdict


def solve():
    cubes = defaultdict(int)

    for line in lines:
        cmd, rest = line.split()
        x, y, z = rest.split(',')
        x_lo = int(x.split('=')[1].split('..')[0])
        x_hi = int(x.split('=')[1].split('..')[1]) + 1
        y_lo = int(y.split('=')[1].split('..')[0])
        y_hi = int(y.split('=')[1].split('..')[1]) + 1
        z_lo = int(z.split('=')[1].split('..')[0])
        z_hi = int(z.split('=')[1].split('..')[1]) + 1

        for x in range(x_lo, x_hi):
            if x < -50 or x > 50:
                continue

            for y in range(y_lo, y_hi):
                if y < -50 or y > 50:
                    continue

                for z in range(z_lo, z_hi):
                    if z < -50 or z > 50:
                        continue

                    
                    if cmd == 'on':
                        cubes[(x, y, z)] = 1
                    elif cmd == 'off':
                        cubes[(x, y, z)] = 0

    print(sum(cubes.values()))
                    

solve()
