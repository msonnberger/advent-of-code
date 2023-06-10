from aocd import numbers, submit

def part1():
    count = sum(x < y for x, y in zip(numbers, numbers[1:]))
    print(f'part 1: {count}')
    #submit(count)


def part2():
    count = sum(x < y for x, y in zip(numbers, numbers[3:]))
    print(f'part 2: {count}')
    #submit(count)

part1()
part2()