from adt.stack import Stack


def infix_to_postfix(expression: str) -> str:
    operators = {
        "**": 3,
        "*": 2, "/": 2,
        "+": 1, "-": 1,
        "(": 0, ")": 0,
    }

    op_stack = Stack()
    output_list = []

    for char in expression.split():
        # print(char)
        if char not in operators:
            output_list.append(char)
        elif char == "(":
            op_stack.push(char)
        elif char == ")":
            top_token = op_stack.pop()
            while top_token != "(":
                output_list.append(top_token)
                top_token = op_stack.pop()
        elif char in operators:
            while (not op_stack.is_empty()) and \
                    (operators[char] <= operators[op_stack.peek()]):
                output_list.append(op_stack.pop())
            op_stack.push(char)

    while not op_stack.is_empty():
        output_list.append(op_stack.pop())

    return " ".join(output_list)


# print(f"A + B * C => {infix_to_postfix('A + B * C')}")
# print(f"A * B + C => {infix_to_postfix('A * B + C')}")
# print(f"A * B + C * D => {infix_to_postfix('A * B + C * D')}")
# print(f"A * B + C * D => {infix_to_postfix('A * B + C * D')}")
# print(f"A + B * C + D => {infix_to_postfix('A + B * C + D')}")
# print(
#     f"( A + B ) * C - ( D - E ) * ( F + G ) => "
#     f"{infix_to_postfix('( A + B ) * C - ( D - E ) * ( F + G )')}"
# )
# print(infix_to_postfix("A * B + C * D"))
# print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))

