import warnings
from typing import Any


class Stack(object):
    """Stack implementation as a list"""

    def __init__(self) -> None:
        """Create new stack"""
        self._items = []

    def __str__(self) -> str:
        return str(self._items)

    def __repr__(self) -> str:
        return repr(self._items)

    def push(self, item) -> None:
        """Add an item to the stack"""
        self._items.append(item)
        return None

    def pop(self) -> Any:
        """Remove an item from the stack"""
        if self._items:
            return self._items.pop()
        warnings.warn("stack is empty")
        return None

    def peek(self) -> Any:
        """Get the value of the top item in the stack"""
        return self._items[-1] if self._items else None

    def is_empty(self) -> bool:
        """Check if stack is empty"""
        return not bool(self._items)  # Pythonic approach

    def size(self) -> int:
        """Get the number of items in the stack"""
        return len(self._items)
