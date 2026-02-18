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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        lastNode = ListNode(float('-inf'), None)
        rootNode = lastNode

        currentHead = head
        while currentHead:
            currentVal = currentHead.val

            if not currentHead.next:
                lastNode.next = currentHead
                break

            #print(f"\nLooking at {currentHead.val}")
            if currentVal == currentHead.next.val:
                #print(f"Found duplicate")
                dupNode = currentHead.next
                while dupNode.next and currentVal == dupNode.next.val:
                    dupNode = dupNode.next

                #currentHead.next = None
                #currentHead = dupNode
                #lastNode.next = dupNode.next
                #lastNode = dupNode.next
                lastNode.next = None
                currentHead = dupNode.next
            else:
                #print(f"No duplicate")
                # Add the new node as it is unique
                lastNode.next = currentHead
                lastNode = currentHead
                # Set next node up to iterate
                currentHead = currentHead.next

        return rootNode.next

if __name__ == '__main__':
    solution = Solution()

    node5 = ListNode(5)
    node4 = ListNode(4, ListNode(4, node5))
    node3 = ListNode(3, ListNode(3, node4))
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)

    newNode = solution.deleteDuplicates(node1)
    #from code import interact; interact(local=dict(globals(), **locals()))
    print(str(newNode))

