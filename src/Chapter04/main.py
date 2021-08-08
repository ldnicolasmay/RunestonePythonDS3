from adt.stack import Stack
from adt.deque import Deque
from adt.ordered_list import OrderedList

# s = Stack()
#
# print(f"{s}")
# print(f"{s.is_empty()}", end="\n\n")
#
# s.push(4)
# print(f"{s}", end="\n\n")
#
# s.push('dog')
# print(f"{s}", end="\n\n")
#
# print(s.peek())
# print(f"{s}", end="\n\n")
#
# s.push(True)
# print(f"{s}", end="\n\n")
#
# print(s.size())
# print(f"{s}", end="\n\n")
#
# print(s.is_empty())
# print(f"{s}", end="\n\n")
#
# s.push(8.4)
# print(f"{s}", end="\n\n")
#
# print(s.pop())
# print(f"{s}", end="\n\n")
#
# print(s.pop())
# print(f"{s}", end="\n\n")
#
# print(s.size())
# print(f"{s}", end="\n\n")


# d = Deque()
#
# print(d.is_empty())
# assert d.is_empty()
# d.add_rear(4)
# d.add_rear("dog")
# d.add_front("cat")
# d.add_front(True)
# print(d.size())
# assert d.size() == 4
# print(d.is_empty())
# assert not d.is_empty()
# d.add_rear(8.4)
# print(d.remove_rear())
# print(d.remove_front())


def run():
    print("foo")
    ol = OrderedList()
    print(f"ol={ol}")


if __name__ == "__main__":
    run()
