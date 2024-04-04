"""
Author: npak243
Solution: It's a simple approach and could be improved
"""


def is_anagram(s: str, t: str) -> bool:
    """
    https://leetcode.com/problems/valid-anagram/
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


print(is_anagram("rat", "cat"))
