from aocd import lines
from sympy import solve, parse_expr

nums = {}

for line in lines:
    name, val = line.split(": ")

    if val.isdigit():
        nums[name] = int(val)
    else:
        l, op, r = val.split(" ")
        nums[name] = (op, l, r)


def calc(name, s=None):
    if type(nums[name]) == int or nums[name] == "x":
        return nums[name]

    op, l, r = nums[name]
    lval, rval = calc(l, s), calc(r, s)

    if s is None:
        return int(eval(str(lval) + op + str(rval)))

    return s + f"({lval} {op} {rval})"


print(f"part 1: {calc('root')}")

nums["humn"] = "x"
_, l, r = nums["root"]
nums["root"] = ("-", l, r)
sympy_eq = parse_expr("Eq(" + calc("root", "") + ", 0)")
print(f"part 2: {solve(sympy_eq)[0]}")
