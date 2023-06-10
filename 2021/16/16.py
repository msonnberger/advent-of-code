from aocd import data

version_sum = 0

def solve():
    bits = str(bin(int(data, 16)))[2:]
    val, _ = parse_packet(bits, 0)
    print(f"part 1: {version_sum}")
    print(f"part 2: {val}")

def parse_packet(bits, i):
    global version_sum

    if i >= len(bits):
        return

    version = int(bits[i : i + 3], 2)
    version_sum += version
    type_id = int(bits[i + 3 : i + 6], 2)
    
    if type_id == 4:
        val, end = parse_literal(bits, i + 6)
        return val, end
    else:
        len_type = int(bits[i + 6], 2)
        sub_vals = []
        sub_start = -1

        if len_type == 0:
            total_length = int(bits[i + 7 : i + 22], 2)
            sub_start = i + 22

            while sub_start < i + 22 + total_length:
                val, sub_start = parse_packet(bits, sub_start)
                sub_vals.append(val)
        else:
            sub_count = int(bits[i + 7 : i + 18], 2)
            sub_start = i + 18
            for _ in range(sub_count):
                val, sub_start = parse_packet(bits, sub_start)
                sub_vals.append(val)

        match(type_id):
            case 0:
                val = sum(sub_vals)
            case 1:
                val = 1
                for value in sub_vals:
                    val *= value
            case 2:
                val = min(sub_vals)
            case 3:
                val = max(sub_vals)
            case 5:
                val = 1 if sub_vals[0] > sub_vals[1] else 0
            case 6:
                val = 1 if sub_vals[0] < sub_vals[1] else 0
            case 7:
                val = 1 if sub_vals[0] == sub_vals[1] else 0

    return val, sub_start

def parse_literal(bits, start):
    i = start
    value = ""
    group = bits[i : i + 5]

    while True:
        value += group[1:]
        
        if group[0] == '0':
            break

        i += 5
        group = bits[i : i + 5]

    value = int(value, 2)
    return value, i + 5

solve()