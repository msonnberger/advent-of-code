from itertools import zip_longest
from aocd import data
from functools import cmp_to_key


def compare(left, right):
    match left, right:
        case int(), int():
            if left < right:
                return -1
            if right < left:
                return 0
        case list(), list():
            for l, r in zip_longest(left, right):
                if l is None:
                    return -1
                if r is None:
                    return 0

                if res := compare(l, r):
                    return -1
                if res == False:
                    return 0
        case int(), list():
            return compare([left], right)
        case list(), int():
            return compare(left, [right])


pairs = [list(map(eval, block.splitlines())) for block in data.split("\n\n")]
total = sum([i + 1 for i, pair in enumerate(pairs) if compare(*pair) == -1])


packets = list(map(eval, filter(lambda line: line != "", data.splitlines())))
packets.extend([[[2]], [[6]]])
packets.sort(key=cmp_to_key(compare))
decoder = (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)

print(f"part 1: {total}")
print(f"part 2: {decoder}")
