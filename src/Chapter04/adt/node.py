from typing import Any


class Node(object):
    """"""


    def __init__(self, data: Any):
        self._data = data
        self._next_node = None

    def get_data(self) -> Any:
        return self._data

    def set_data(self, data) -> None:
        self._data = data

    data = property(get_data, set_data)

    def get_next_node(self):
        return self._next_node

    def set_next_node(self, next_node) -> None:
        self._next_node = next_node

    next_node = property(get_next_node, set_next_node)

    def __str__(self):
        return f"{str(self.data)},{str(self.next_node)}"
