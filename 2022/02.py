from aocd import lines

abc = "ABC"
xyz = "XYZ"
length = len(abc)
games = [(abc.index(line.split()[0]), xyz.index(line.split()[1])) for line in lines]


def calc_score(opponent, me):
    score = me + 1

    if (me - opponent) % 3 == 1:
        score += 6
    if me == opponent:
        score += 3

    return score


score1 = sum([calc_score(opponent, me) for opponent, me in games])
score2 = sum([calc_score(opponent, (opponent + me - 1) % 3) for opponent, me in games])

print(f"part 1: {score1}")
print(f"part 2: {score2}")
