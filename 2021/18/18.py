import itertools
import math
from functools import reduce
from ast import literal_eval
from aocd import lines


def add_left(num, n):
    if n is None:
        return num
    if isinstance(num, int):
        return num + n
    return [add_left(num[0], n), num[1]]


def add_right(num, n):
    if n is None:
        return num
    if isinstance(num, int):
        return num + n
    return [num[0], add_right(num[1], n)]


def explode(num, n=4):
    if isinstance(num, int):
        return False, None, num, None
    if n == 0:
        return True, num[0], 0, num[1]
    a, b = num
    exploded, left, a, right = explode(a, n - 1)
    if exploded:
        return True, left, [a, add_left(b, right)], None
    exploded, left, b, right = explode(b, n - 1)
    if exploded:
        return True, None, [add_right(a, left), b], right
    return False, None, num, None


def split(num):
    if isinstance(num, int):
        if num >= 10:
            return True, [num // 2, math.ceil(num / 2)]
        return False, num
    a, b = num
    changed, a = split(a)
    if changed:
        return True, [a, b]
    changed, b = split(b)
    return changed, [a, b]


def add(a, b):
    x = [a, b]
    while True:
        changed, _, x, _ = explode(x)
        if changed:
            continue
        changed, x = split(x)
        if not changed:
            break
    return x


def magnitude(num):
    if isinstance(num, int):
        return num
    return 3 * magnitude(num[0]) + 2 * magnitude(num[1])


lines = list(map(literal_eval, lines))
print("part 1:", magnitude(reduce(add, lines)))
print("part 2:", max(magnitude(add(a, b)) for a, b in itertools.permutations(lines, 2)))
