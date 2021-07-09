import warnings
from typing import Any


class Stack(object):
    """
    Stack implementation as a list
    """

    def __init__(self) -> None:
        """
        Create new stack
        """
        self._items = []
        return None

    def __str__(self) -> str:
        return str(self._items)

    def __repr__(self) -> str:
        return repr(self._items)

    def push(self, item) -> None:
        """
        Add an item to the stack
        """
        self._items.append(item)
        return None

    def pop(self) -> Any:
        """
        Remove an item from the stack
        """
        if self._items:
            return self._items.pop()
        warnings.warn(f"stack is empty")
        return None

    def peek(self) -> Any:
        """
        Get the value of the top item in the stack
        """
        return self._items[-1]

    def is_empty(self) -> bool:
        """
        Check if stack is empty
        """
        # return len(self._items) == 0  # traditional approach
        return not bool(self._items)  # Pythonic approach

    def size(self) -> int:
        """
        Get the numer of items in the stack
        """
        return len(self._items)

