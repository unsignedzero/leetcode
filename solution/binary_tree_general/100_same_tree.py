from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        r""" We will return early if there's a False we see
        """

        # Check none
        if not p and not q:
            return True # If the node is empty can't traverse further down
        # Check unequal value
        if (p and not q) or (not p and q):
            return False

        if not p.val == q.val:
            return False

        left = True
        # Empty both left
        if not p.left and not q.left:
            pass
        # Unequal left
        elif (p.left and not q.left) or (not p.left and q.left):
            return False
        # Recurse Left
        else:
            left = self.isSameTree(p.left, q.left)

        right = True
        # Empty both right
        if not p.right and not q.right:
            pass
        # Unequal right
        elif (p.right and not q.right) or (not p.right and q.right):
            return False
        # Recurse right
        else:
            right = self.isSameTree(p.right, q.right)

        return all((left,  right))


