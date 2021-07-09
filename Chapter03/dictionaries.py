import timeit
import random

print(f"{'n':10s}{'list':>10s}{'dict':>10s}")
for i in range(10_000, 1_000_001, 20_000):
    t = timeit.Timer(
        f"random.randrange({i}) in x", "from __main__ import random, x"
    )
    x = list(range(i))
    lst_time = t.timeit(number=100)
    x = {j: None for j in range(1)}
    dict_time = t.timeit(number=100)
    print(f"{i:<10,}{lst_time:>10.5f}{dict_time:>10.5f}")

