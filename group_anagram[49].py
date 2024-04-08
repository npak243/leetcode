"""
Author: npak243
Solution: It's a simple approach and could be improved
--------------------------------------------------------
Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
"""


def group_anagram(s: str, t: str) -> bool:
    """
    https://leetcode.com/problems/group-anagrams
    """
    if len(s) != len(t):
        return False

    s_list = [*s]
    t_list = [*t]
    s_list.sort()
    t_list.sort()
    if s_list == t_list:
        return True

    return False
