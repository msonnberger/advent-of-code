from aocd import lines
from statistics import median

pairs = {'(':')', '[':']','{':'}','<':'>'}
error_values = {')':3, ']':57, '}':1197, '>':25137}
closing_values = {')':1, ']':2, '}':3, '>':4}

def solve():
    error_score = 0
    closing_scores = []

    for line in lines:
        corrupt = False
        stack = []
        closing_score = 0

        for c in line:
            if c in pairs.keys():
                stack.append(pairs[c])
            elif c in pairs.values():
                if stack.pop() != c:
                    error_score += error_values[c]
                    corrupt = True

        if not corrupt:
            for c in reversed(stack):
                closing_score *= 5
                closing_score += closing_values[c]

            closing_scores.append(closing_score)

    print(f"part 1: {error_score}")
    print(f"part 2: {median(closing_scores)}")

solve()