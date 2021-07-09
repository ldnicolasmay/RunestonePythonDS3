from stack import Stack


def reverse_string_1(string: str) -> str:
    forward_stack = Stack()
    for letter in string:
        forward_stack.push(letter)

    backward_list = []
    while not forward_stack.is_empty():
        backward_list.append(forward_stack.pop())

    return "".join(backward_list)


print(reverse_string_1("foobar"))
print(reverse_string_1("supercalifragilisticexpialidocious"))

assert reverse_string_1("foobar") == "raboof"

