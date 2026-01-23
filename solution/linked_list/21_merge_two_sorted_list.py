# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode],
                            list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1:
            return list2
        elif not list2:
            return list1

        originalTail = ListNode()
        tail = originalTail

        # Combine
        list1Ptr, list2Ptr = list1, list2
        while list1Ptr and list2Ptr:
            if list1Ptr.val < list2Ptr.val:
                tail.next = list1Ptr
                tail = list1Ptr
                list1Ptr = list1Ptr.next
            else:
                tail.next = list2Ptr
                tail = list2Ptr
                list2Ptr = list2Ptr.next

        while list1Ptr:
            tail.next = list1Ptr
            tail = list1Ptr
            list1Ptr = list1Ptr.next

        while list2Ptr:
            tail.next = list2Ptr
            tail = list2Ptr
            list2Ptr = list2Ptr.next

        return originalTail.next

