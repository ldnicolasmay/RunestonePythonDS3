from adt.stack import Stack
from infix_to_postfix import infix_to_postfix


def postfix_eval(expression: str) -> str:
    operators = {
        "*": 2, "/": 2,
        "+": 1, "-": 1,
        "(": 0, ")": 0,
    }

    calc_stack = Stack()

    for char in expression.split():
        # print(char)
        if char not in operators:
            calc_stack.push(char)
        elif char in operators:
            b = calc_stack.pop()
            a = calc_stack.pop()
            calc_stack.push(eval(f"{a} {char} {b}"))

    return str(calc_stack.pop())


# print(
#     f"2 + 3 * 4 => "
#     f"{infix_to_postfix('2 + 3 * 4')} = "
#     f"{postfix_eval(infix_to_postfix('2 + 3 * 4'))}"
# )
# print(
#     f"2 * 3 + 4 => "
#     f"{infix_to_postfix('2 * 3 + 4')} = "
#     f"{postfix_eval(infix_to_postfix('2 * 3 + 4'))}"
# )
# print(
#     f"2 * 3 + 4 * 5 => "
#     f"{infix_to_postfix('2 * 3 + 4 * 5')} = "
#     f"{postfix_eval(infix_to_postfix('2 * 3 + 4 * 5'))}"
# )
# print(
#     f"2 + 3 * 4 + 5 => "
#     f"{infix_to_postfix('2 + 3 * 4 + 5')} = "
#     f"{postfix_eval(infix_to_postfix('2 + 3 * 4 + 5'))}"
# )
# print(
#     f"( 2 + 3 ) * 4 - ( 5 - 6 ) * ( 7 + 8 ) => "
#     f"{infix_to_postfix('( 2 + 3 ) * 4 - ( 5 - 6 ) * ( 7 + 8 )')} = "
#     f"{postfix_eval(infix_to_postfix('( 2 + 3 ) * 4 - ( 5 - 6 ) * ( 7 + 8 )'))}"
# )

