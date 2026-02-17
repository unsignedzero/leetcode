# Definition for singly-linked list.
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
    def reverseGroup(self, node: ListNode, k: int) -> tuple(ListNode):
        """ Given k nodes, we want to reverse them.

        For example, we will do k == 4, so we will see k = 1,2,3 in the loop
        A -> B -> C -> D -> X

        We need to store the left value and only current (A) to iterate through
        store left, store current
        k = 1| > A -> B -> C -> D -> X
        k = 2| > B -> A; >A -> C -> D -> X
        k = 3| > C -> B -> A; >A -> D
        After k = 3| >D -> C -> B -> A -> X; > A -> X
        """

        finalNode = node
        previousNode = finalNode
        for _ in range(1, k):
            leftNode = finalNode.next
            leftNode.next, finalNode.next = previousNode, leftNode.next
            previousNode = leftNode

        return (leftNode, finalNode)

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or not head.next or k == 1:
            return head

        newHead = None
        oldCurrentHead = currentHead = head

        while True:

            # Check if current group has enough nodes to swap
            checkNode = currentHead
            for _ in range(1, k):
                if checkNode.next:
                    checkNode = checkNode.next
                else:
                    # If not quit
                    return newHead if newHead else head

            #print(f"Check node {checkNode}")

            # Process k nodes-group
            leftNode, currentHead = self.reverseGroup(currentHead, k)

            #print(f">>>Left node {leftNode.val}, currentHead {currentHead.val}")
            # Get the final head if we need it
            if not newHead:
                newHead = leftNode
            else:
                # This links the groups together that are remaining, else we lose links
                # between groups
                oldCurrentHead.next = leftNode
            oldCurrentHead = currentHead

            # Advance to the next group
            currentHead = currentHead.next
            if not currentHead :
                break

        return newHead if newHead else head

if __name__ == '__main__':
    solution = Solution()

    node5 = ListNode(5)
    node4 = ListNode(4, node5)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)

    #print(node1)

    #leftNode, newNode = solution.reverseGroup(node1, 2)
    #oldNewNode = newNode
    #leftNode, newNode = solution.reverseGroup(node3, 2)
    #oldNewNode.next = leftNode

    finalList = solution.reverseKGroup(node1, 2)
    #finalList = solution.reverseKGroup(node1, 5)
    print(finalList)

