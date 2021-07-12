from stack import Stack

# 233 // 8 = 29 rem 1
#  29 // 8 =  3 rem 5
#   3 // 8 =  0 rem 3
# -------------------
# 233 => 351

# 233 // 16 = 14 rem 9
#  14 // 16 =  0 rem E
# --------------------
# 233 => E9

def _stack_reversed_2_str(stack: Stack) -> str:
    unstacked_list = []
    while not stack.is_empty():
        unstacked_list.append(str(stack.pop()))

    return "".join(unstacked_list)


def _dec_digit_to_base_digit(dec_digit: int) -> str:
    #         0         1         2         3
    #         01234567890123456789012345678901
    #          b     o       x
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUV"
    return digits[dec_digit]


def _dec_2_base_helper(dec_num: int, base: int, stack: Stack) -> str:
    if dec_num == 0:
        result = _stack_reversed_2_str(stack)
    else:
        quotient = dec_num // base
        remainder = dec_num % base
        stack.push(_dec_digit_to_base_digit(remainder))
        result = _dec_2_base_helper(quotient, base, stack)

    return result


def dec_2_base(dec_num: int, base: int) -> str:
    if base < 2 or 32 < base:
        raise ValueError("base must be between 2 and 32 (inclusive)")
    return _dec_2_base_helper(dec_num, base, Stack())


print(f"dec_2_base(233, 8)={dec_2_base(233, 8)}")
print(f"dec_2_base(233, 16)={dec_2_base(233, 16)}")
print(f"dec_2_base(123456789, 16)={dec_2_base(123456789, 16)}")
# print(f"dec_2_base(233, 1)={dec_2_base(233, 1)}")
print(f"dec_2_base(233, 17)={dec_2_base(233, 17)}")
print(f"dec_2_base(26, 26)={dec_2_base(26, 26)}")

print("---")

for i in range(2, 33):
    print(f"dec_2_base({i}, {i})={dec_2_base(i, i)}")

print("---")

for i in range(2, 33):
    print(f"dec_2_base({i*i-1}, {i})={dec_2_base(i*i-1, i)}")

