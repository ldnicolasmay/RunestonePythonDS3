from timeit import Timer


def test0():
    pass

def test1():
    l = []
    for i in range(1000):
        l = l + [i]


def test2():
    l = []
    for i in range(1000):
        l.append(i)


def test3():
    l = [i for i in range(1000)]


def test4():
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

