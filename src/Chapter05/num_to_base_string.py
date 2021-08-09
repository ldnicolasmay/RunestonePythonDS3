def to_str(n: int, base: int) -> str:
    digits = "0123456789abcdef"
    if n == 0:
        return ""
    else:
        quotient = n // base
        remainder = n % base
        return to_str(quotient, base) + digits[remainder]


def to_str_acc(n: int, base: int, acc: str = "") -> str:
    digits = "0123456789abcdef"
    if n == 0:
        return acc
    else:
        quotient = n // base
        remainder = n % base
        return to_str_acc(quotient, base, digits[remainder] + acc)


print(to_str(769, 10))
print(to_str(769, 16))
print(to_str(769, 2))
print(to_str_acc(769, 2))
print(to_str(1453, 16))
print(to_str_acc(1453, 16))