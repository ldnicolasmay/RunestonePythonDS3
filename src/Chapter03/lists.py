from timeit import Timer


def test0() -> None:
    pass


# Appending elements to a list

def test1() -> None:
    l = []
    for i in range(1000):
        l = l + [i]

def test2() -> None:
    l = []
    for i in range(1000):
        l.append(i)

def test3() -> None:
    l = [i for i in range(1000)]

def test4() -> None:
    l = list(range(1000))


t0 = Timer("test0()", "from __main__ import test0")
t1 = Timer("test1()", "from __main__ import test1")
t2 = Timer("test2()", "from __main__ import test2")
t3 = Timer("test3()", "from __main__ import test3")
t4 = Timer("test4()", "from __main__ import test4")

print(f"empty function: {t0.timeit(number=1000):14.5f} ms")
print(f"concatenation: {t1.timeit(number=1000):15.5f} ms")
print(f"appending: {t2.timeit(number=1000):19.5f} ms")
print(f"list comprehension: {t3.timeit(number=1000):10.5f} ms")
print(f"list range: {t4.timeit(number=1000):18.5f} ms")


# Popping elements from a list

list_1 = list(range(2_000_000))
list_2 = list(range(2_000_000))

pop_zero = Timer("list_1.pop(0)", "from __main__ import list_1")
pop_end = Timer("list_2.pop()", "from __main__ import list_2")

# print(f"pop(0): {pop_zero.timeit(number=1000):10.5f} ms")
# print(f"pop(): {pop_end.timeit(number=1000):11.5f} ms")

print(f"{'n':10s}{'pop(0)':>15s}{'pop()':>15s}")
for i in range(1_000_000, 10_000_001, 1_000_000):
    list_1 = list(range(i))
    pop_zero_t = pop_zero.timeit(number=1000)
    list_2 = list(range(i))
    pop_end_t = pop_end.timeit(number=1000)
    print(f"{i:<10d}{pop_zero_t:>15.5f}{pop_end_t:>15.5f}")

