#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # Helps debug when printing
    def __str__(self):
        stringBuffer = []
        stringBuffer.append(f"Nodes {self.val}")
        nextNode = self.next
        while nextNode:
            stringBuffer.append(f"{nextNode.val}")
            nextNode = nextNode.next

        return "->".join(stringBuffer)


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or not head.next or k == 0:
            return head

        # Get Length
        listLength = 1

        curNode = head
        while curNode.next:
            curNode = curNode.next
            listLength += 1
        lastNode = curNode

        # Get snippet length
        rotationValue = k % listLength

        # If it's a no-op, just empty early
        if rotationValue == 0:
            return head

        # Get right node where we want to slice it
        curNode = head
        for _ in range(1, listLength-rotationValue):
            curNode = curNode.next
        spliceNode = curNode

        # Wire the end
        lastNode.next = head
        # Set our new head
        newHead = spliceNode.next
        # Cut the splice point
        spliceNode.next = None

        return newHead

if __name__ == '__main__':
    node3 = ListNode(3)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)
    solution = Solution()

    result = solution.rotateRight(node1, 2)
    #result = solution.rotateRight(node1, 2000000000)
    print(result)

