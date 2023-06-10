from aocd import lines


def snafu_to_dec(snafu):
    digits = []

    for c in snafu:
        if c == "-":
            digits.append(-1)
        elif c == "=":
            digits.append(-2)
        else:
            digits.append(int(c))

    return sum([5**i * d for i, d in enumerate(reversed(digits))])


def dec_to_snafu(d):
    if d:  # if d is not zero
        a, b = divmod(d + 2, 5)
        return dec_to_snafu(a) + "=-012"[b]
    else:
        return ""  # base case


print(dec_to_snafu(sum([snafu_to_dec(snafu) for snafu in lines])))
