from adt.stack import Stack


def to_str(n: int, base: int) -> str:
    digits = "0123456789abcdef"
    if n == 0:
        return ""
    else:
        quotient = n // base
        remainder = n % base
        return to_str(quotient, base) + digits[remainder]


print(to_str(769, 10))
print(to_str(769, 16))
print(to_str(769, 2))
print(to_str(1453, 16))


def to_str_acc(n: int, base: int, acc: str = "") -> str:
    digits = "0123456789abcdef"
    if n == 0:
        return acc
    else:
        quotient = n // base
        remainder = n % base
        return to_str_acc(quotient, base, digits[remainder] + acc)


print(to_str_acc(769, 2))
print(to_str_acc(1453, 16))


def to_str_stack(n: int, base: int) -> str:
    digits = "0123456789abcdef"
    r_stack = Stack()

    while n > 0:
        remainder = n % base
        r_stack.push(digits[remainder])
        n = n // base

    res = ""
    while not r_stack.is_empty():
        res = res + str(r_stack.pop())

    return res


print(to_str_stack(769, 10))
print(to_str_stack(769, 2))
print(to_str_stack(1453, 16))
print(to_str_stack(10, 2))

# run from ~/Documents/Learning/DataStructuresAndAlgorithms/RunestonePythonDS3
# $ python3 -m src.Chapter05.num_to_base_string
