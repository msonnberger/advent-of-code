from aocd import data

cards = data.splitlines()
points = 0
num_of_cards = [1] * len(cards)

for i, line in enumerate(cards):
    line = line.split(":")[1]
    winning, have = line.split("|")
    matches = len(set(winning.split()) & set(have.split()))

    if matches > 0:
        points += 2 ** (matches - 1)

    for j in range(matches):
        num_of_cards[i + j + 1] += num_of_cards[i]


print(f"part 1: {points}")
print(f"part 2: {sum(num_of_cards)}")
