"""
Author: npak243
Solution: It's a simple approach and could be improved
--------------------------------------------------------
Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""
from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    """
    https://leetcode.com/problems/contains-duplicate/
    """
    if len(set(nums)) == len(nums):
        return False
    return True
