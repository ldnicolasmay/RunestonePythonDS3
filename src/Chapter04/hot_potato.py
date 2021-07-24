from typing import List

from adt.queue import Queue  # works


def hot_potato(names_list: List[str], num: int) -> str:
    names_q = Queue()
    for name in names_list:
        names_q.enqueue(name)

    while names_q.size() > 1:
        print(f"This round's participants: {names_q}")
        for i in range(num):
            names_q.enqueue(names_q.dequeue())
        print(f"This round's loser: {names_q.dequeue()}")

    return names_q.dequeue()


# winner: str = hot_potato(["Alice", "Bob", "Carol", "Dave", "Elaine"], 3)
winner: str = hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7)
print(f"Winner: {winner}")
