# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def countHelper(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0

            return 1 + max(countHelper(root.left), countHelper(root.right))

        if root is None:
            return 0

        return 1 + max(countHelper(root.left), countHelper(root.right))
