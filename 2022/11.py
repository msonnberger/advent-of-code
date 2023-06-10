from aocd import data
import math


def parse_data():
    monkeys = []

    for block in data.split("\n\n"):
        lines = block.splitlines()
        monkey = {}
        monkey["items"] = [int(x) for x in lines[1].split(": ")[1].split(", ")]
        op_string = (
            lines[2]
            .split(": ")[1]
            .replace("new", "x")
            .replace("old", "x")
            .replace(" = ", ": ")
        )
        monkey["op"] = eval("lambda " + op_string)
        monkey["test"] = int(lines[3].split()[-1])
        monkey["if_true"] = int(lines[4].split()[-1])
        monkey["if_false"] = int(lines[5].split()[-1])
        monkey["inspect_count"] = 0

        monkeys.append(monkey)

    return monkeys


def run_n_rounds(n, part2):
    monkeys = parse_data()
    lcm = math.lcm(*[m["test"] for m in monkeys])

    for _ in range(n):
        for monkey in monkeys:
            for i, item in enumerate(monkey["items"]):
                monkey["items"][i] = monkey["op"](item)

                if not part2:
                    monkey["items"][i] //= 3

                monkey["items"][i] %= lcm
                if monkey["items"][i] % monkey["test"] == 0:
                    monkeys[monkey["if_true"]]["items"].append(monkey["items"][i])
                else:
                    monkeys[monkey["if_false"]]["items"].append(monkey["items"][i])

                monkey["inspect_count"] += 1

            monkey["items"] = []

    sort = sorted(monkeys, key=lambda d: d["inspect_count"], reverse=True)
    return sort[0]["inspect_count"] * sort[1]["inspect_count"]


print(f"part 1: {run_n_rounds(20, False)}")
print(f"part 2: {run_n_rounds(10000, True)}")
