from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        newSum = targetSum - root.val
        if (not root.left and not root.right) and newSum == 0:
            return True
        else:
            return any((self.hasPathSum(root.left, newSum),
                        self.hasPathSum(root.right, newSum)))

