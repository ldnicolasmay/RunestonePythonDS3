from adt.deque import Deque


def check_palindrome(text: str) -> bool:
    deque = Deque()

    for char in text:
        deque.add_rear(char)

    while deque.size() > 1:
        front_char = deque.remove_front()
        rear_char = deque.remove_rear()
        if front_char != rear_char:
            return False

    return True


print(check_palindrome("radar"))
print(check_palindrome("asdfghjkllkjhgfdsa"))
print(check_palindrome("samnas"))
