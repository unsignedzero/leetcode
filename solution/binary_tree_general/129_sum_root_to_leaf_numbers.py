from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def traverseDigitTree(self, root: Optional[TreeNode], currentValue: str, values: List[str]):
        r""" Add the current int string and continue down the tree.
        We leave the summation to the parent caller function.
        """

        finalString = f"{currentValue}{root.val}"
        if not root.left and not root.right:
            values.append(finalString)
            return

        if root.left:
            self.traverseDigitTree(root.left, finalString, values)
        if root.right:
            self.traverseDigitTree(root.right, finalString, values)

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        r""" Parent recursive function that checks if we should recurse
        """

        if not root:
            return 0

        result = []
        self.traverseDigitTree(root, "", result)

        return sum(map(int, result))

