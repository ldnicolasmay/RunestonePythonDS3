from typing import Any

from node import Node


class UnorderedList(object):
    """
    Linked list wherein ite are placed by user
    """

    def __init__(self) -> None:
        self.head: Node = None

    def __str__(self) -> str:
        return str(self.head)

    def is_empty(self) -> bool:
        return self.head is None

    def size(self) -> int:
        current_node: Node = self.head
        current_pos: int = 0

        while current_node is not None:
            current_pos = current_pos + 1
            current_node = current_node.next_node

        return current_pos

    def search(self, item: Any) -> bool:
        current_node: Node = self.head

        while current_node is not None:
            if current_node.data == item:
                return True
            current_node = current_node.next_node

        return False

    def index(self, item: Any) -> int:
        current_node = self.head
        current_pos = 0

        while current_node is not None:
            if current_node.data == item:
                return current_pos
            current_node = current_node.next_node
            current_pos = current_pos + 1

        return -1

    def add(self, item: Any):
        new_node = Node(item)
        new_node.next_node = self.head
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

    def append(self, item: Any):
        previous_node = None
        current_node: Node = self.head
        new_node = Node(item)

        while current_node is not None:
            previous_node = current_node
            current_node = current_node.next_node

        if previous_node is None:
            self.head = new_node
        else:
            previous_node.next_node = new_node

    def insert(self, pos: int, item: Any):
        previous_node = None
        current_node: Node = self.head
        current_pos: int = 0
        new_node = Node(item)

        while current_node is not None:
            print(f"prev={previous_node}, curr={current_node}")
            if current_pos == pos:
                if previous_node is None and current_node is not None:    # at head
                    self.head = new_node
                    new_node.next_node = current_node
                    break
                else:                                                     # in middle
                    previous_node.next_node = new_node
                    new_node.next_node = current_node
                    break
            else:
                previous_node = current_node
                current_node = current_node.next_node
            current_pos = current_pos + 1

        if previous_node is None and current_node is None:   # list is empty
            self.head = new_node
        if previous_node is not None and current_node is None:
            previous_node.next_node = new_node

    def pop(self, pos: int = None) -> None:
        previous_node = None
        current_node = self.head

        updated_pos = pos if pos else (self.size() - 1)

        if current_node is None:
            raise ValueError("cannot pop item from empty list")

        current_pos = 0
        return_val = None

        while current_node is not None:
            if current_pos == updated_pos:
                return_val = current_node.data
                break
            previous_node = current_node
            current_node = current_node.next_node
            current_pos = current_pos + 1

        if current_node is None:
            raise ValueError(f"`pos` is not in range")
        elif previous_node is None:
            self.head = current_node.next_node
            return return_val
        else:
            previous_node.next_node = current_node.next_node
            return return_val
