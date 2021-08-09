from typing import List


def loop_sum_list(nums: List[int]) -> int:
    acc: int = 0
    for num in nums:
        acc = acc + num
    return acc


print(loop_sum_list([1, 2, 3]))


def recurse_sum_list(nums: List[int]) -> int:
    current_sum = nums[0] + recurse_sum_list(nums[1:]) if nums else 0
    return current_sum


print(recurse_sum_list([1, 2, 3]))
