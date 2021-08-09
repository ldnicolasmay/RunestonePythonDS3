from sys import maxsize


def reverse(s: str) -> str:
    return reverse(s[1:]) + s[0] if s else ""


def remove_white(s: str) -> str:
    return (
        s.lower()
            .replace(" ", "", maxsize)
            .replace(",", "", maxsize)
            .replace(".", "", maxsize)
            .replace("'", "", maxsize)
            .replace("-", "", maxsize)
    )


def is_palindrome(s: str) -> bool:
    return remove_white(s) == reverse(remove_white(s))


print(is_palindrome("x"))
print(is_palindrome("kayak"))
print(is_palindrome("Live not on evil"))
print(is_palindrome("madam i'm adam"))
