"""
Author: npak243
Solution: It's a simple approach and could be improved
"""
from typing import List


def two_sum_native(nums: List[int], target: int) -> List[int]:
    """
    https://leetcode.com/problems/two-sum/
    Native approach
    """
    for idx in range(len(nums) - 1):
        for idx2 in range(idx+1, len(nums)):
            if nums[idx] + nums[idx2] == target:
                return [idx, idx2]


def two_sum_better(nums: List[int], target: int) -> List[int]:
    """
    https://leetcode.com/problems/two-sum/
    Approach:
    - Devide input into 2 list by target/2
    - Use binary search to find the suitable number
    """
    pass
