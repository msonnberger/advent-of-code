from aocd import data
import portion

seeds = list(map(int, data.splitlines()[0].split(":")[1].split()))
maps = data.split("\n\n")[1:]
min_location = float("inf")


for seed in seeds:
    source = seed

    for m in maps:
        lines = m.splitlines()[1:]

        for line in lines:
            dest_start, source_start, length = map(int, line.split())

            if source_start <= source < source_start + length:
                source = dest_start + source - source_start
                break

    min_location = min(min_location, source)


print(f"part 1: {min_location}")


### Part 2

interval = portion.closedopen
ranges = [interval(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]
min_location = float("inf")

for _range in ranges:
    source = _range

    for m in maps:
        lines = m.splitlines()[1:]
        dest = source

        for line in lines:
            dest_start, source_start, n = map(int, line.split())
            source_overlap = source & interval(source_start, source_start + n)

            if source_overlap != portion.empty():
                diff = dest_start - source_start
                lower, upper = source_overlap.lower, source_overlap.upper
                dest -= source_overlap
                dest |= interval(lower + diff, upper + diff)

        source = dest

    min_location = min(min_location, source.lower)

print(f"part 2: {min_location}")
