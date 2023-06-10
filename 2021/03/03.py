from aocd import submit, lines

size = len(lines[0])

def update_counts(numbers = lines):
    zero_count = [0] * size
    one_count = [0] * size
    
    for i in range(size):
        zero_count[i] = "".join(line[i] for line in numbers).count('0')
        one_count[i] = "".join(line[i] for line in numbers).count('1')

    return zero_count, one_count

def part1():
    gam = eps = ''
    zero_count, one_count = update_counts(lines)
    
    for i in range(len(zero_count)):
        if one_count[i] > zero_count[i]:
            gam += '1'
            eps += '0'
        else:
            gam += '0'
            eps += '1'

    result = int(gam, 2) * int(eps, 2)
    print(f'part 1: {result}')
    #submit(result)

def part2():
    o2list = list(set(lines))
    co2list = list(set(lines))

    while len(o2list) > 1:
        for i in range(size):
            if (len(o2list) == 1):
                break

            zero_count, one_count = update_counts(o2list)
            
            j = 0
            while j < len(o2list):

                if (one_count[i] > zero_count[i] and o2list[j][i] == '0'):
                    o2list.remove(o2list[j])
                elif (zero_count[i] > one_count[i] and o2list[j][i] == '1'):
                    o2list.remove(o2list[j])
                elif (one_count[i] == zero_count[i] and o2list[j][i] == '0'):
                    o2list.remove(o2list[j])
                else:
                    j += 1

    while len(co2list) > 1:
        for i in range(size):
            if (len(co2list) == 1):
                break
            
            zero_count, one_count = update_counts(co2list)

            j = 0
            while j < len(co2list):
                if (one_count[i] < zero_count[i] and co2list[j][i] == '0'):
                    co2list.remove(co2list[j])
                elif (zero_count[i] < one_count[i] and co2list[j][i] == '1'):
                    co2list.remove(co2list[j])
                elif (one_count[i] == zero_count[i] and co2list[j][i] == '1'):
                    co2list.remove(co2list[j])
                else:
                    j += 1

    result = int(co2list[0], 2) * int(o2list[0], 2)
    print(f'part 2: {result}')
    #submit(result)

part1()
part2()