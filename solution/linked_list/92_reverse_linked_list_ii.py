# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        # Edge cases for bad input.
        if not head or left > right or left == right:
            return head

        # We need to find "left" if it exists. We make a node to deal with starting on the left node
        newRootnode = ListNode(next=head)
        currentNodeIndex = 0

        currentNode = newRootnode
        # We advance until we get the node "left" of left
        while currentNode and currentNodeIndex < left - 1:
            currentNode = currentNode.next
            currentNodeIndex += 1

        # We run out of nodes
        if not currentNode:
            return newRootnode.next

        nextNode = currentNode.next
        for _ in range(right - left):
            """ Swap the node links
            newNode = nextNode.next
            if not newNode:
                break
            nextNode.next = newNode.next
            newNode.next = currentNode.next
            currentNode.next = newNode
            """

            newNode = nextNode.next
            if not nextNode.next:
                break
            currentNode.next, nextNode.next, newNode.next = newNode, newNode.next, currentNode.next


        return newRootnode.next

