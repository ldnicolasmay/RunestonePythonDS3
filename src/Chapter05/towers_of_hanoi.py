# 1 disc:
# 1  1 -> 2

# 2 discs:
# 1  0 -> 1
# 2  0 -> 2
# 3  1 -> 2

# 3 discs:
# 1  1 -> 2
# 2  1 -> 0
# 3  2 -> 0
# 4  1 -> 2
# 5  0 -> 1
# 6  0 -> 2
# 7  1 -> 2

# 4 discs:
#  1  0 -> 1
#  2  0 -> 2
#  3  1 -> 2
#  4  0 -> 1
#  5  2 -> 0
#  6  2 -> 1
#  7  0 -> 1
#  8  0 -> 2   # 3 discs:
#  9  1 -> 2   # 1  1 -> 2
# 10  1 -> 0   # 2  1 -> 0
# 11  2 -> 0   # 3  2 -> 0
# 12  1 -> 2   # 4  1 -> 2   # 2 discs:
# 13  0 -> 1   # 5  0 -> 1   # 1  0 -> 1
# 14  0 -> 2   # 6  0 -> 2   # 2  0 -> 2   # 1 disc:
# 15  1 -> 2   # 7  1 -> 2   # 3  1 -> 2   # 1  1 -> 2

# 4 discs:
#  1  0 -> 1
#  2  0 -> 2
#  3  1 -> 2
#  4  0 -> 1
#  5  2 -> 0
#  6  2 -> 1
#  7  0 -> 1
#  8  0 -> 2   # 3 discs:
#  9  1 -> 2   # 1  0 -> 2
# 10  1 -> 0   # 2  0 -> 1
# 11  2 -> 0   # 3  2 -> 1
# 12  1 -> 2   # 4  0 -> 2   # 2 discs:
# 13  0 -> 1   # 5  1 -> 0   # 1  0 -> 1
# 14  0 -> 2   # 6  1 -> 2   # 2  0 -> 2   # 1 disc:
# 15  1 -> 2   # 7  0 -> 2   # 3  1 -> 2   # 1  0 -> 2

from typing import Dict
from adt.stack import Stack


def foo(
    towers: Dict[str, Stack],
    n: int,
    from_pole: str,
    with_pole: str,
    to_pole: str
) -> Dict[str, Stack]:

    if n == 1:
        # print(f"if    towers={towers}; n={n}")
        print(f"pop from_pole -> push to_pole")
        towers[to_pole].push(towers[from_pole].pop())
    else:
        # print(f"else1 towers={towers}; n={n}")
        towers = foo(towers, n - 1, from_pole, to_pole, with_pole)
        # print(f"else2 towers={towers}; n={n}")
        print(f"pop from_pole -> push to_pole")
        towers[to_pole].push(towers[from_pole].pop())
        # print(f"else3 towers={towers}; n={n}")
        towers = foo(towers, n - 1, with_pole, from_pole, to_pole)

    return towers


f_pole = Stack()
w_pole = Stack()
t_pole = Stack()

my_n = 4

for i in reversed(range(my_n)):
    f_pole.push(i)

ts = {"from_pole": f_pole, "with_pole": w_pole, "to_pole": t_pole}

print("\nStart state:")
print(ts)

new_ts = foo(ts, n=my_n, from_pole="from_pole", with_pole="with_pole", to_pole="to_pole")

print("\nFinal state:")
print(new_ts)
