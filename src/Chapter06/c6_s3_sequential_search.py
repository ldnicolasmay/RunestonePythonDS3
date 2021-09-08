from typing import Any, List


def sequential_search(a_list: List[Any], item: Any) -> bool:
    pos = 0

    while pos < len(a_list):
        if a_list[pos] == item:
            return True
        else:
            pos = pos + 1

    return False


test_list_1 = [54, 26, 93, 17, 77, 31, 44, 55, 20, 65]
# print(sequential_search(test_list_1, 13)); print()
# print(sequential_search(test_list_1, 17)); print()


def ordered_sequential_search(a_list: List[Any], item: Any) -> bool:
    pos = 0

    while pos < len(a_list):
        print(f"pos={pos}")
        if a_list[pos] == item:
            return True
        elif a_list[pos] > item:
            return False
        else:
            pos = pos + 1

    return False


test_list_2 = sorted(test_list_1)
print(test_list_2); print()
print(ordered_sequential_search(test_list_2, 13)); print()
print(ordered_sequential_search(test_list_2, 17)); print()
print(ordered_sequential_search(test_list_2, 41)); print()
