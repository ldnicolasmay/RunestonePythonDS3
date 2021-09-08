from typing import Any, List
import random

# test_list_1 = [54, 26, 93, 17, 77, 31, 44, 55, 20, 65]

n = 10_000
random.seed(1234)
test_list_1 = random.sample(range(100_000), n)
test_list_2 = sorted(test_list_1)


def binary_search_helper(a_list: List[Any], item: Any, first: int, last: int) -> bool:
    mid = first + (last - first) // 2
    print(f"first={first}; mid={mid}; last={last}")
    if first >= last:
        return False
    elif item == a_list[mid]:
        return True
    elif item < a_list[mid]:
        return binary_search_helper(a_list, item, first, mid)
    elif item > a_list[mid]:
        return binary_search_helper(a_list, item, mid + 1, last)


def binary_search(a_list: List[Any], item: Any) -> bool:
    return binary_search_helper(a_list, item, 0, len(a_list))


print(test_list_2); print()
print(binary_search(test_list_2, 4)); print()
print(binary_search(test_list_2, 5)); print()
print(binary_search(test_list_2, 7)); print()
print(binary_search(test_list_2, 14)); print()
print(binary_search(test_list_2, 16)); print()
print(binary_search(test_list_2, 17)); print()
print(binary_search(test_list_2, 19)); print()
print(binary_search(test_list_2, 27)); print()
print(binary_search(test_list_2, 31)); print()
print(binary_search(test_list_2, 32)); print()
print(binary_search(test_list_2, 451)); print()
print(binary_search(test_list_2, 69820)); print()
print(binary_search(test_list_2, 99994)); print()
print(binary_search([], 13)); print()
