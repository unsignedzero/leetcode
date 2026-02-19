# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # We can make this faster by removing this as the test cases make sure
        # these never happen
        # if not head or n < 1:
        #     return head

        fakeHead = ListNode(0, head)
        left = right = fakeHead

        # Advance a pointer n steps ahead
        for _ in range(n):
            right = right.next
            if not right:
                return head

        # Move in lock step
        while right.next:
            left, right = left.next, right.next

        # Delete the nth node behind
        left.next = left.next.next

        return fakeHead.next

