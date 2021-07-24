from adt.stack import Stack

# 233 // 2 = 166 rem 1
# 116 // 2 =  58 rem 0
#  58 // 2 =  29 rem 0
#  29 // 2 =  14 rem 1
#  14 // 2 =   7 rem 0
#   7 // 2 =   3 rem 1
#   3 // 2 =   1 rem 1
#   1 // 2 =   0 rem 1
# --------------------
# 233 => 11101001

#   4 // 2 =   2 rem 0
#   2 // 2 =   1 rem 0
#   1 // 2 =   0 rem 1
# --------------------
#   4 => 100


def _stack2str(stack: Stack) -> str:
    unstacked_list = []
    while not stack.is_empty():
        unstacked_list.append(str(stack.pop()))

    return "".join(unstacked_list)


def _dec2bin_helper(dec_num: int, stack: Stack) -> str:
    if dec_num == 0:
        result = "0b" + _stack2str(stack)
    else:
        quotient = dec_num // 2
        remainder = dec_num % 2
        stack.push(remainder)
        result = _dec2bin_helper(quotient, stack)

    return result


def dec2bin(dec_num: int) -> str:
    return _dec2bin_helper(dec_num, Stack())


print(f"dec2bin(4)={dec2bin(4)}")
print(f"bin(4)=    {bin(4)}")

print("---")

print(f"dec2bin(233)={dec2bin(233)}")
print(f"bin(233)=    {bin(233)}")

for i in range(1, 10_000):
    # print(dec2bin(i), bin(i))
    assert dec2bin(i) == bin(i)


# print(0x100)  # hex -> dec
# print(0o100)  # oct -> dec
# print(0b100)  # bin -> dec

# print(hex(100))  # dec -> hex str
# print(oct(100))  # dec -> oct str
# print(bin(100))  # dec -> bin str

# print(int("0x100", 16))  # hex str -> int
# print(int("0o100", 8))   # oct str -> int
# print(int("0b100", 2))   # bin str -> int

