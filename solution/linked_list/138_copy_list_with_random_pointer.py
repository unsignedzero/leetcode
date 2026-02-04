from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        r""" Seems a lot easier to do a 2 pass with one just making elements
        and the 2nd wiring it all in versus splitting the wire apart.
        """

        newHead = head

        elementMap = {}

        # Build linked list
        while newHead != None:
            value = newHead.val
            newNode = Node(value)
            elementMap[newHead] = newNode
            newHead = newHead.next

        # Wire everything in
        newHead = head
        while newHead != None:
            newNode = elementMap[newHead]
            newNode.next = elementMap.get(newHead.next)
            newNode.random = elementMap.get(newHead.random)
            newHead = newHead.next

        return elementMap.get(head)

