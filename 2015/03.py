from aocd import data

dirs = {"^": 1j, "v": -1j, ">": 1, "<": -1}


def get_visited(data):
    pos = 0
    visited = {pos}
    for dir in data:
        pos += dirs[dir]
        visited.add(pos)

    return visited


print(f"part 1: {len(get_visited(data))}")
print(f"part 2: {len(get_visited(data[::2]) | get_visited(data[1::2]))}")
