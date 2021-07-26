import warnings
from typing import Any

class Deque(object):
    """Deque implementation as a list"""

    def __init__(self) -> None:
        """Create new deque"""
        self._items = []

    def __str__(self) -> str:
        return str(self._items)

    def __repr__(self) -> str:
        return repr(self._items)

    def add_front(self, item) -> None:
        """Add item to front of deque"""
        self._items.insert(0, item)

    def add_rear(self, item) -> None:
        """Add item to rear of deque"""
        self._items.append(item)

    def remove_front(self) -> Any:
        """Remove item from front of deque"""
        if self._items:
            return self._items.pop(0)
        warnings.warn("deque is empty")
        return None

    def remove_rear(self) -> Any:
        """Remove item from rear of deque"""
        if self._items:
            return self._items.pop()
        warnings.warn("deque is empty")
        return None

    def is_empty(self) -> bool:
        """Check if deque is empty"""
        return not bool(self._items)

    def size(self) -> int:
        """Get the number of items in the deque"""
        return len(self._items)

