"""
Author: npak243
Solution: It's a simple approach and could be improved
--------------------------------------------------------
Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        https://leetcode.com/problems/reverse-string/
        Do not return anything, modify s in-place instead.
        """
        def helper(s: List[str], start, end):
            if start >= end:
                return

            s[start], s[end] = s[end], s[start]

            return helper(s, start + 1, end - 1)

        helper(s, 0, len(s) - 1)
