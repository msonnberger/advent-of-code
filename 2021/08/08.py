from aocd import lines

def part1():
    count = 0
    for line in lines:
        out = line.split(" | ")
        for o in out.split():
            if len(o) in [2, 3, 4, 7]:
                count += 1

    print(f"part 1: {count}")

def part2():
    total = 0

    for line in lines:
        digits = ["null"] * 10
        inp, out = line.split(" | ")
        for i in line.replace(" | ", " ").split():
            if len(i) == 2:
                digits[1] = i
            elif len(i) == 3:
                digits[7] = i
            elif len(i) == 4:
                digits[4] = i
            elif len(i) == 7:
                digits[8] = i

        for i in line.replace(" | ", " ").split():
            if len(i) == 6:
                if (set(digits[4]).issubset(i)):
                    digits[9] = i
                elif (set(digits[7]).issubset(i)):
                    digits[0] = i
                else:
                    digits[6] = i
            elif len(i) == 5:
                if (set(digits[7]).issubset(i)):
                    digits[3] = i
                elif len(set(digits[4]).intersection(set(i))) == 3:
                    digits[5] = i
                else:
                    digits[2] = i

        digit_str = ""
        digits = [set(x) for x in digits]
        for o in out.split():
            digit_str += str(digits.index(set(o)))

        total += int(digit_str)

    print(f"part 2: {total}")

part1()
part2()