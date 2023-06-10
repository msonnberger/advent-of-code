from aocd import lines
import functools

p1_pos = int(lines[0].split()[-1])
p2_pos = int(lines[1].split()[-1])

def part1():
    global p1_pos, p2_pos
    p1_score, p2_score = 0, 0
    dice = 1

    while p1_score < 1000 and p2_score < 1000:
        p1_move = 3 * dice + 3
        p1_pos = (p1_pos + p1_move - 1) % 10 + 1
        p1_score += p1_pos
        dice += 3

        if p1_score >= 1000:
            break
        
        p2_move = 3 * dice + 3
        p2_pos = (p2_pos + p2_move - 1) % 10 + 1
        p2_score += p2_pos
        dice += 3

    return min(p1_score, p2_score) * (dice - 1)


memo = {}

@functools.cache
def part2(pos1, score1, pos2, score2):
    if score1 >= 21:
        return (1, 0)

    if score2 >= 21:
        return (0, 1)

    if (pos1, score1, pos2, score2) not in memo:
        a, b = 0, 0
        for r1 in (1, 2, 3):
            for r2 in (1, 2, 3):
                for r3 in (1, 2, 3):
                    new_pos1 = (pos1 + r1 + r2 + r3 - 1) % 10 + 1
                    c, d = part2(pos2, score2, new_pos1, score1 + new_pos1)
                    a += d
                    b += c
        
        memo[pos1, score1, pos2, score2] = (a, b)
    
    return memo[pos1, score1, pos2, score2]

print('part 1:', part1())
print('part 2:', max(part2(8, 0, 10, 0)))