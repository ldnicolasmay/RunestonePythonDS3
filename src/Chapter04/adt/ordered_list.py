from typing import Any

from node import Node


class OrderedList(object):
    """

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
        new_node = Node(item)
        previous_node = None
        current_node = self.head

        while current_node is not None:
            if previous_node is None and item < current_node.data:
                self.head = new_node
                new_node.next_node = current_node
                break
            elif previous_node is None and item > current_node.data:
                previous_node = current_node
                current_node = current_node.next_node
                continue
            elif previous_node.data < item < current_node.data:
                previous_node.next_node = new_node
                new_node.next_node = current_node
                break
            elif current_node.data < item and current_node.next_node is None:
                current_node.next_node = new_node
                break
            previous_node = current_node
            current_node = current_node.next_node

        if current_node is None:
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
        pass


listX = OrderedList()
print(f"listX={listX}")

listX.add(5)
print(f"listX={listX}")

listX.add(4)
print(f"listX={listX}")

listX.add(1)
print(f"listX={listX}")

listX.add(0)
print(f"listX={listX}")

listX.add(6)
print(f"listX={listX}")

listX.add(2)
print(f"listX={listX}")

listX.add(3)
print(f"listX={listX}")
