from typing import Dict

from adt.stack import Stack


def solve_hanoi_towers(
    towers: Dict[str, Stack],
    n: int,
    from_pole: str,
    with_pole: str,
    to_pole: str,
) -> Dict[str, Stack]:
    if n == 1:
        towers[to_pole].push(towers[from_pole].pop())
    else:
        towers = solve_hanoi_towers(towers, n - 1, from_pole, to_pole, with_pole)
        towers[to_pole].push(towers[from_pole].pop())
        towers = solve_hanoi_towers(towers, n - 1, with_pole, from_pole, to_pole)

    return towers


f_pole = Stack()
w_pole = Stack()
t_pole = Stack()

my_n = 4
for i in reversed(range(my_n)):
    f_pole.push(i)

ts = {"from_pole": f_pole, "with_pole": w_pole, "to_pole": t_pole}
new_ts = solve_hanoi_towers(ts, my_n, "from_pole", "with_pole", "to_pole")

print(f"ts={ts}")
print(f"new_ts={new_ts}")
