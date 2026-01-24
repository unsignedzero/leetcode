from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        r""" Simple solution for traversal
        """

        #print(f"{preorder=}, {inorder=}")
        if not preorder or not inorder:
            return None

        if len(preorder) == 1:
            return TreeNode(val=preorder[0])

        centerVal = preorder[0]
        rootNode = TreeNode(val=centerVal)

        splitPoint = inorder.index(centerVal)
        leftInorder, rightInorder = inorder[:splitPoint], inorder[1+splitPoint:]
        #print(f"{splitPoint=}, {leftInorder=}, {rightInorder=}")

        newPreorder = preorder.copy()
        newPreorder.remove(centerVal)

        splitPoint = len(leftInorder)
        leftPreorder, rightPreorder = newPreorder[:splitPoint], newPreorder[splitPoint:]
        #print(f"{splitPoint=}, {leftPreorder=}, {rightPreorder=}")

        if leftPreorder and leftInorder:
            rootNode.left = self.buildTree(leftPreorder, leftInorder)
        if rightPreorder and rightInorder:
            rootNode.right = self.buildTree(rightPreorder, rightInorder)

        return rootNode

if __name__ == '__main__':
    solution = Solution()
    a = (solution.buildTree([3,9,20,15,7], [9,3,15,20,7]))
    from code import interact; interact(local=dict(globals(), **locals()))
