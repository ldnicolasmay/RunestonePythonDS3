import warnings
from typing import Any

from node import Node


class UnorderedList(object):

    def __init__(self) -> None:
        self.head = None

    def __str__(self) -> str:
        return str(self.head)

    def is_empty(self) -> bool:
        return self.head is None

    def add(self, item: Any) -> None:
        temp_node = Node(item)
        temp_node.next_node = self.head
        self.head = temp_node

    def size(self) -> int:
        current_node = self.head
        count = 0
        while current_node is not None:
            count = count + 1
            current_node = current_node.next_node

        return count

    def search(self, item: Any) -> bool:
        current_node = self.head
        while current_node is not None:
            if current_node.data == item:
                return True
            current_node = current_node.next_node
        
        return False

    def remove(self, item: Any) -> None:
        previous_node = None
        current_node = self.head

        while current_node is not None:
            if current_node.data == item:
                break
            previous_node = current_node
            current_node = current_node.next_node

        if current_node is None:                    # reached end; data not found
            raise ValueError(f"{item} is not in the list")
        elif previous_node is None:                 # data is in head
            self.head = current_node.next_node      # connect head to 2nd node
        else:                                       # data is in non-head
            previous_node.next = current_node.next  # connect previous node to next node

    def append(self, item: Any) -> None:
        current_node = self.head

        if current_node is None:
            self.head = Node(item)
        else:
            while current_node.next_node is not None:
                current_node = current_node.next_node
            current_node.next_node = Node(item)

    def insert(self, pos: int, item: Any) -> None:
        previous_node: Node = None
        current_node: Node = self.head
        current_pos = 0
        list_size = self.size()

        if pos > list_size:
            raise ValueError(f"pos value {pos} is greater than list length")
        elif pos == 0:
            temp_node = Node(item)
            temp_node.next_node = current_node
            self.head = temp_node
        else:
            while current_node is not None:
                if current_pos == pos:
                    temp_node = Node(item)
                    previous_node.next_node = temp_node
                    temp_node.next_node = current_node
                    break
                elif current_pos == list_size - 1:
                    temp_node = Node(item)
                    current_node.next_node = temp_node
                    break

                current_pos = current_pos + 1
                previous_node = current_node
                current_node = current_node.next_node

    def index(self, item: Any) -> int:
        current_node = self.head
        current_pos = 0

        while current_node is not None:
            if current_node.data == item:
                return current_pos

            current_node = current_node.next_node
            current_pos = current_pos + 1

        return -1

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


listX = UnorderedList()
print(f"listX={listX}")

# print(f"listX.pop()={listX.pop()}")
# print(f"listX={listX}")

listX.append("a")
print(f"listX={listX}")
print(listX.pop(0))
print(f"listX={listX}")

listX.append("a")
listX.append("b")
print(f"listX={listX}")
print(listX.pop(0))
print(f"listX={listX}")

# print(listX.pop(3))
# print(f"listX={listX}")

print(listX.pop())
print(f"listX={listX}")


# list0 = UnorderedList()
# print(f"list0={list0}")
# print("... adding node ...")
# list0.add(1)
# print(f"list0={list0}")
# print("... adding node ...")
# list0.add(2)
# print(f"list0={list0}")
# print(f"list0.size()={list0.size()}")
# print(f"list0.search(2)={list0.search(2)}")
# print(f"list0.search(1)={list0.search(1)}")
# print(f"list0.search(0)={list0.search(0)}")
#
# list1 = UnorderedList()
# print(f"list1={list1}")
# try:
#     list1.remove(1)
# except ValueError as e:
#     print(e)
# print(f"list1={list1}")
# list1.add(1)
# print(f"list1={list1}")
# list1.remove(1)
# print(f"list1={list1}")
# list1.add(1)
# list1.add(2)
# print(f"list1={list1}")
# list1.remove(2)
# print(f"list1={list1}")

# list2 = UnorderedList()
# list2.append("a")
# print(f"list2={list2}")
# list2.append("b")
# print(f"list2={list2}")
# list2.insert(0, "foo")
# print(f"list2={list2}")
# list2.insert(3, "bar")
# print(f"list2={list2}")
# list2.insert(0, "baz")
# print(f"list2={list2}")
# list2.insert(2, "qux")
# print(f"list2={list2}")
#
# print(list2.index("baz"))  # expect 0
# print(list2.index("foo"))
# print(list2.index("qux"))
# print(list2.index("a"))
# print(list2.index("b"))
# print(list2.index("bar"))
# print(list2.index("xyzzy"))
#
# print(f"list2={list2}")
# print(list2.pop())
# print(f"list2={list2}")
#
# list3 = UnorderedList()
# try:
#     print(list3.pop())
# except ValueError as e:
#     print(e)
# list3.add(1)
# print(list3.pop())
# print(f"list3={list3}")
# list3.add(2)
# print(f"list3={list3}")
# print(list3.pop())
# print(f"list3={list3}")
