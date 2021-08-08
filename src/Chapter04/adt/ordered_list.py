from typing import Any

from node import Node


class OrderedList(object):
    """
    Linked list wherein items stay ordered
    """

    def __init__(self):
        self.head = None

    def __str__(self) -> str:
        return str(self.head)

    def is_empty(self) -> bool:
        return not bool(self.head)

    def size(self) -> int:
        current_node: Node = self.head
        counter: int = 0

        while current_node is not None:
            current_node = current_node.next_node
            counter = counter + 1

        return counter

    def search(self, item: Any) -> bool:
        current_node: Node = self.head

        while current_node is not None:
            if current_node.data == item:
                return True
            if current_node.data > item:
                return False
            current_node = current_node.next_node

        return False

    def index(self, item: Any) -> int:
        current_node = self.head
        current_pos = 0

        while current_node is not None:
            if current_node.data == item:
                return current_pos
            if current_node.data > item:
                return -1
            current_node = current_node.next_node
            current_pos = current_pos + 1

        return -1

    def add(self, item: Any):
        previous_node = None
        current_node = self.head
        new_node = Node(item)

        while current_node is not None and current_node.data < item:
            previous_node = current_node
            current_node = current_node.next_node

        if previous_node is None:  # head
            new_node.next_node = self.head
            self.head = new_node
        elif previous_node is not None and current_node is None:  # end
            current_node = new_node
            previous_node.next_node = current_node
        else:  # middle
            previous_node.next_node = new_node
            new_node.next_node = current_node

        if current_node is None:  # empty list
            self.head = new_node

    def remove(self, item: Any):
        previous_node = None
        current_node: Node = self.head

        if current_node is None:           # empty list
            raise ValueError("Cannot remove item from empty list")

        while current_node is not None:
            if current_node.data == item:
                if previous_node is None:  # only one item in list
                    self.head = current_node.next_node
                else:                      # more than one item in list
                    previous_node.next_node = current_node.next_node
            previous_node = current_node
            current_node = current_node.next_node

    def pop(self, pos: int = None) -> Any:
        pos = pos if pos is not None else self.size() - 1
        previous_node = None
        current_node = self.head
        current_pos = 0

        if current_node is None:
            raise ValueError("cannot pop item from empty list")

        if pos < 0 or self.size() - 1 < pos:
            raise ValueError(f"pos of {pos} is out of range")

        while current_node is not None:
            if pos == current_pos:
                if previous_node is None:  # head
                    self.head = current_node.next_node
                    return current_node.data
                else:
                    previous_node.next_node = current_node.next_node
                    return current_node.data
            else:
                previous_node = current_node
                current_node = current_node.next_node
                current_pos = current_pos + 1
