"""
Author: npak243
Solution: It's a simple approach and could be improved
"""
from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    """
    https://leetcode.com/problems/contains-duplicate/
    """
    if len(set(nums)) == len(nums):
        return False
    return True
