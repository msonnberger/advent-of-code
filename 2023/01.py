from aocd import data

words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def solve(part2=False):
    total = 0
    for line in data.splitlines():
        digits_only = ""
        for i, ch in enumerate(line):
            if part2:
                for j, word in enumerate(words):
                    if line[i:].startswith(word):
                        digits_only += str(j + 1)

            if ch.isdigit():
                digits_only += ch

        total += int(digits_only[0] + digits_only[-1])

    return total


print(f"part 1: {solve()}")
print(f"part 2: {solve(True)}")
