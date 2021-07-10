from stack import Stack


def is_balanced(
    input_string: str,
    symbols: str = "()[]{}<>",
) -> bool:

    assert len(symbols) % 2 == 0
    left_symbols = symbols[0::2]
    right_symbols = symbols[1::2]
    # Zip into dicts for O(1) time 'contains' (`in`) and 'gets' (`[]`)
    left_symbols_dict = dict(zip(left_symbols, right_symbols))
    right_symbols_dict = dict(zip(right_symbols, left_symbols))

    stack = Stack()

    for symbol in input_string:
        if symbol in left_symbols_dict:
            stack.push(symbol)
        elif symbol in right_symbols_dict:
            matching_left_symbol = right_symbols_dict[symbol]
            if stack.is_empty() or stack.peek() != matching_left_symbol:
                return False
            else:
                stack.pop()

    return stack.is_empty()


print(is_balanced("()"))  # expect True
print(is_balanced("(]"))  # expect False
print(is_balanced("(()"))  # expect False
print(is_balanced("())"))  # expect False
print(is_balanced("(a(bc(def)))"))  # expect True
print(is_balanced("[[[[a]bc]def]ghij]", "[]"))  # expect True
print(is_balanced("([{<abcdef>ghij}klmno]pqrstuv)"))  # expect True
print(is_balanced("([{[abc}def]ghij)"))  # expect False
print(is_balanced("([{<a}bc}def]ghij)"))  # expect False
print(is_balanced(":a-bc&cde*=;", ":;-=&*"))  # expect True

