# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return str(self.val)

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        r""" A better solution would be to find the path of p and q and compare the longest
        common "prefix" using depth-first search.
        """

        pathP, pathQ = [], []

        def printPath(currentPath: list(TreeNode)):
            return list(map(str, currentPath))

        def advanceDown(findSet: set(TreeNode), currentNode: 'TreeNode', currentPath: list(TreeNode)):
            r""" Depth-first search to find the current nodes p and q
            """

            #print(f"On {currentNode.val=}, {printPath(currentPath)}")
            nonlocal pathP, pathQ
            if currentNode in findSet:
                if currentNode == p:
                    #print(f"Found p {printPath(currentPath)}")
                    pathP = currentPath.copy()
                else:
                    #print(f"Found q {printPath(currentPath)}")
                    pathQ = currentPath.copy()

            if pathP and pathQ:
                return

            if currentNode.left:
                #print(">>Going left")
                currentPath.append(currentNode.left)
                advanceDown(findSet, currentNode.left, currentPath)
                currentPath.pop()
            if currentNode.right:
                #print(">>Going right")
                currentPath.append(currentNode.right)
                advanceDown(findSet, currentNode.right, currentPath)
                currentPath.pop()

        advanceDown(set((p, q)), root, [root])
        #print(f">>>>In {printPath(pathP)} and {printPath(pathQ)}")

        finalCommonNode = None
        for left, right in zip(pathP, pathQ):
            if left == right:
                finalCommonNode = left
            else:
                break

        return finalCommonNode

if __name__ == '__main__':
    node5 = TreeNode(5)
    node1 = TreeNode(1)
    node3 = TreeNode(3)
    node3.left = node5
    node3.right = node1
    solution = Solution()

    print(solution.lowestCommonAncestor(node3, node5, node1))

