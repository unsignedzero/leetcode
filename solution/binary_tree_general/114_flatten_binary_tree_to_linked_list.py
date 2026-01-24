from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        if not root:
            return None

        if not root.left and not root.right:
            return root

        print(f"Looking at {root.val}")
        left = self.flatten(root.left)
        right = self.flatten(root.right)

        if left:
            root.left = None
            root.right = left
        if right:
            if not root.right:
                root.right = right
            # Make sure we don't revisit the same right node
            elif right != root.right:

                curNode = root.right
                while curNode.right:
                    curNode = curNode.right
                curNode.right = right

        return root

if __name__ == '__main__':
    solution = Solution()

    node6 = TreeNode(6)
    node5 = TreeNode(5, None, node6)
    node4 = TreeNode(4)
    node3 = TreeNode(3)
    node2 = TreeNode(2, node3, node4)
    node1 = TreeNode(1, node2, node5)

    solution.flatten(node1)
    curNode = node1
    while curNode:
        print(curNode.val)
        curNode = curNode.right
