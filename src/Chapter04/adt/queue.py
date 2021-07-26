import warnings
from typing import Any

class Queue(object):
    """Queue implementation as a list"""

    def __init__(self) -> None:
        """Create new queue"""
        self._items = []

    def __str__(self) -> str:
        return str(self._items)

    def __repr__(self) -> str:
        return repr(self._items)

    def enqueue(self, item) -> None:
        """Add item to rear of queue"""
        self._items.insert(0, item)

    def dequeue(self) -> Any:
        """Remove item from front of queue"""
        if self._items:
            return self._items.pop()
        warnings.warn("queue is empty")
        return None

    def is_empty(self) -> bool:
        """Check if queue is empty"""
        return not bool(self._items)

    def size(self) -> int:
        """Get the number of items in the queue"""
        return len(self._items)

