from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        r""" Simple solution for traversal
        """

        #print(f"{postorder=}, {inorder=}")
        if not inorder or not postorder:
            return None

        if len(inorder) == 1:
            return TreeNode(val=inorder[0])

        centerVal = postorder[-1]
        rootNode = TreeNode(val=centerVal)

        splitPoint = inorder.index(centerVal)
        leftInorder, rightInorder = inorder[:splitPoint], inorder[1+splitPoint:]
        #print(f"{splitPoint=}, {leftInorder=}, {rightInorder=}")

        newPostorder = postorder.copy()
        newPostorder.remove(centerVal)

        splitPoint = len(leftInorder)
        leftPostorder, rightPostorder = newPostorder[:splitPoint], newPostorder[splitPoint:]
        #print(f"{splitPoint=}, {leftPostorder=}, {rightPostorder=}")

        if leftPostorder and leftInorder:
            rootNode.left = self.buildTree(leftInorder, leftPostorder)
        if rightPostorder and rightInorder:
            rootNode.right = self.buildTree(rightInorder, rightPostorder)

        return rootNode


if __name__ == '__main__':
    solution = Solution()
    a = (solution.buildTree([9,3,15,20,7], [9,15,7,20,3]))
    #from code import interact; interact(local=dict(globals(), **locals()))
