from aocd import data
from collections import Counter
import functools

hands = [(hand, int(bid)) for hand, bid in (l.split() for l in data.splitlines())]


def get_strength(count):
    distinct = len(count)

    # handle two pair and full house (where number of distinct cards does not correspond to hand type)
    if not any(c == 6 - distinct for c in count.values()):
        distinct += 0.5

    return -distinct


def get_count(cards, part2):
    count = Counter(cards)

    if not part2 or len(count) == 1 or not "J" in count:
        return count

    first, second = count.most_common(2)

    if first[0] == "J":
        first = second

    count[first[0]] += count["J"]
    del count["J"]

    return count


def cmp(a, b, part2=False):
    a_count, b_count = get_count(a, part2), get_count(b, part2)
    a_strength, b_strength = get_strength(a_count), get_strength(b_count)

    if a_strength != b_strength:
        return a_strength - b_strength

    values = "23456789TJQKA" if not part2 else "J23456789TQKA"

    for i in range(5):
        a_value, b_value = values.index(a[i]), values.index(b[i])

        if a_value != b_value:
            return a_value - b_value

    return 0


hands.sort(key=functools.cmp_to_key(lambda a, b: cmp(a[0], b[0], part2=False)))
total = sum([hand[1] * (i + 1) for i, hand in enumerate(hands)])
print(f"part 1: {total}")

hands.sort(key=functools.cmp_to_key(lambda a, b: cmp(a[0], b[0], part2=True)))
total = sum([hand[1] * (i + 1) for i, hand in enumerate(hands)])
print(f"part 2: {total}")
