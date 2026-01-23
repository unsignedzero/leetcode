from typing import Optional

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        left = right = 0
        if root.left:
            left = 1 + self.maxDepth(root.left)
        if root.right:
            right = 1 + self.maxDepth(root.right)

        return max(left, right)

