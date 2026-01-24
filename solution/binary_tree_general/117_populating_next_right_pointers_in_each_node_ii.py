from itertools import pairwise

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __str__(self):
        return f"{self.val}"

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        r""" Simple width scan solution
        """

        if not root:
            return None

        currentRow = [root]
        while currentRow:
            #print(f"{currentRow=}")

            newRow = []
            for currentNode in currentRow:
                newRow.extend((currentNode.left, currentNode.right))

            # Remove "null" pointers
            newRow = list(filter(None, newRow))
            #print(f"{newRow=}")

            for left, right in pairwise(newRow):
                left.next = right

            currentRow = newRow

        return root

if __name__ == '__main__':
    left = Node(2)
    right = Node (3)
    top = Node(1, left, right)

    solution = Solution()
    print(solution.connect(top))
