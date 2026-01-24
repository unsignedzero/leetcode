from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        r""" Swap all left and right nodes of a tree
        """

        # Reject on an empty node
        if not root:
            return

        # If we have a node, root.left and root.right are defined
        # but values maybe None
        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left, root.right = root.right, root.left

        return root

