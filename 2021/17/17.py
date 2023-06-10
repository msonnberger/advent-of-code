from aocd import data

x_min, x_max = data.split(', ')[0].split('=')[1].split('..')
y_min, y_max = data.split(', ')[1].split('=')[1].split('..')
x_min = int(x_min)
x_max = int(x_max)
y_min = int(y_min)
y_max = int(y_max)


def solve():
    max_height = 0
    count = 0

    for vx0 in range(abs(x_max) + 1):
        for vy0 in range(-abs(y_min), abs(y_min) + 1):
            x, y = 0, 0
            vx, vy = vx0, vy0
            curr_max_height = 0
            while x <= x_max and y >= y_min:
                x += vx
                y += vy
                curr_max_height = max(curr_max_height, y)
                if vx > 0:
                    vx -= 1
                elif vx < 0:
                    vx += 1
                
                vy -= 1

                if x_min <= x <= x_max and y_min <= y <= y_max:
                    max_height = max(max_height, curr_max_height)
                    count += 1
                    break

    print(f"part 1: {max_height}")
    print(f"part 2: {count}")

solve()