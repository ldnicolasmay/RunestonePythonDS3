from math import inf

nums = [4, -3, 2, 5, 1, 0, 7]

def get_min_quadratic(ns):
    the_min = inf
    for i in ns:
        for j in ns:
            if i < j and i < the_min:
                the_min = i
            elif j < i and j < the_min:
                the_min = j

    return the_min

print(get_min_quadratic(nums))


def get_min_linear(ns):
    the_min = inf
    for n in ns:
        the_min = n if n < the_min else the_min

    return the_min

print(get_min_linear(nums))

