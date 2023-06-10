from aocd import data
import re

stacks = [
    ["D", "T", "R", "B", "J", "L", "W", "G"],
    ["S", "W", "C"],
    ["R", "Z", "T", "M"],
    ["D", "T", "C", "H", "S", "P", "V"],
    ["G", "P", "T", "L", "D", "Z"],
    ["F", "B", "R", "Z", "J", "Q", "C", "D"],
    ["S", "B", "D", "J", "M", "F", "T", "R"],
    ["L", "H", "R", "B", "T", "V", "M"],
    ["Q", "P", "D", "S", "V"],
]

instructions = data.split("\n\n")[1]
regex = re.compile(r"move (\d+) from (\d+) to (\d+)")


def solve(part2=False):
    stacks_copy = [stack.copy() for stack in stacks]

    for line in instructions.split("\n"):
        amount, fro, to = regex.match(line).groups()
        amount, fro, to = int(amount), int(fro) - 1, int(to) - 1

        if part2:
            stacks_copy[to].extend(stacks_copy[fro][-amount:])

        for _ in range(amount):
            val = stacks_copy[fro].pop()

            if not part2:
                stacks_copy[to].append(val)

    return "".join([stack[-1] for stack in stacks_copy])


print(f"part 1: {solve(part2=False)}")
print(f"part 2: {solve(part2=True)}")
