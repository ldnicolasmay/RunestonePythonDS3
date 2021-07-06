import time

def sum_of_n(n):
    the_sum = 0
    for i in range(1, n + 1):
        the_sum = the_sum + i

    return the_sum

print(sum_of_n(10))


def sum_of_n_2(n):
    start = time.time()

    the_sum = 0
    for i in range(1, n + 1):
        the_sum = the_sum + i

    end = time.time()

    return the_sum, end - start

for i in range(5):
    print(f"Sum of %d required %10.7f secdonds" % sum_of_n_2(10000))
for i in range(5):
    print(f"Sum of %d required %10.7f secdonds" % sum_of_n_2(100000))
for i in range(5):
    print(f"Sum of %d required %10.7f secdonds" % sum_of_n_2(1000000))
for i in range(5):
    print(f"Sum of %d required %10.7f secdonds" % sum_of_n_2(10000000))


def sum_of_n_3(n):
    start = time.time()
    the_sum = (n * (n + 1)) / 2
    end = time.time()
    return the_sum, end - start

for i in range(5):
    print(f"Sum of %d required %10.7f secdonds" % sum_of_n_3(10000))
for i in range(5):
    print(f"Sum of %d required %10.7f secdonds" % sum_of_n_3(100000))
for i in range(5):
    print(f"Sum of %d required %10.7f secdonds" % sum_of_n_3(1000000))
for i in range(5):
    print(f"Sum of %d required %10.7f secdonds" % sum_of_n_3(10000000))

