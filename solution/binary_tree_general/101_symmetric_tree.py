from typing import Optional
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def checkSide(self, rootLeft: Optional[TreeNode], rootRight: Optional[TreeNode]) -> bool:
    	r""" Straightforward approach of checking left and right node.
    	"""

        # Check root node
        if not rootLeft and not rootRight:
            return True
        if (rootLeft and not rootRight) or (not rootLeft and rootRight):
            return False
        if rootLeft.val != rootRight.val:
            return False

        # Check Left
        if (not rootLeft.left and rootRight.right) or (rootLeft.left and not rootRight.right):
            return False
        left = self.checkSide(rootLeft.left, rootRight.right)

        # Check Right
        if (not rootLeft.right and rootRight.left) or (rootLeft.right and not rootRight.left):
            return False
        right = self.checkSide(rootLeft.right, rootRight.left)

        return all((left, right))

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if not root or (not root.left and not root.right):
            return True

        return self.checkSide(root.left, root.right)

