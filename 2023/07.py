from aocd import data
from collections import Counter
import functools

hands = [line.split() for line in data.splitlines()]
hands = [tuple([cards, int(bid)]) for cards, bid in hands]


def get_strength(count):
    distinct = len(count)

    # no three of a kind --> two pair
    if distinct == 3 and not any(c == 3 for c in count.values()):
        return 2.5
    # no four of a kind --> full house
    elif distinct == 2 and not any(c == 4 for c in count.values()):
        return 3.5

    return 6 - distinct


def get_count(cards, part2):
    count = Counter(cards)

    if (not part2) or len(count) == 1 or not "J" in count:
        return count

    most_common = count.most_common(1)[0][0]

    if most_common == "J":
        most_common = count.most_common(2)[1][0]

    count[most_common] += count["J"]
    del count["J"]

    return count


def cmp(a, b, part2=False):
    a_count, b_count = get_count(a[0], part2), get_count(b[0], part2)
    a_strength, b_strength = get_strength(a_count), get_strength(b_count)

    if a_strength != b_strength:
        return a_strength - b_strength

    values = "23456789TJQKA" if not part2 else "J23456789TQKA"

    for i in range(5):
        a_value, b_value = values.index(a[0][i]), values.index(b[0][i])

        if a_value != b_value:
            return a_value - b_value

    return 0


hands.sort(key=functools.cmp_to_key(lambda a, b: cmp(a, b, part2=False)))
total = sum([hand[1] * (i + 1) for i, hand in enumerate(hands)])
print(f"part 1: {total}")

hands.sort(key=functools.cmp_to_key(lambda a, b: cmp(a, b, part2=True)))
total = sum([hand[1] * (i + 1) for i, hand in enumerate(hands)])
print(f"part 2: {total}")
