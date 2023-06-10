from aocd import data

def solve(days):
    numbers = [int(x) for x in data.split(',')]
    counts = [numbers.count(i) for i in range(9)]

    for _ in range(days):
        new_count = counts[0]
        counts[0] = 0

        for i in range(1, len(counts)):
            counts[i - 1] += counts[i]
            counts[i] = 0

        counts[6] += new_count
        counts[8] += new_count

    print(f"{days} days: {sum(counts)}")


solve(80)
solve(256)