from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        r""" An interesting solution using the slow/faster pointer solution.
        """
        slowPointer = fastPointer = head

        while fastPointer and fastPointer.next:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next
            if slowPointer == fastPointer:
                return True
        return False


    def hasCycle2(self, head: Optional[ListNode]) -> bool:
        r"""A brute-force solution to check which nodes we have seen
        """

        seen = set()
        currentNode = head

        while True:
            if currentNode is None:
                break
            if currentNode in seen:
                return True
            seen.add(currentNode)
            currentNode = currentNode.next


        return False

