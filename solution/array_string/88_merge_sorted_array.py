from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        r""" This is just the final step in a merge sort that we will need to do.
        The only thing different is that the first list `nums1` has enough
        space to fit everything and we don't need to allocate another list.
        """

        if n == 0:
            return nums1

        leftPos, rightPos = (m - 1), (n - 1)
        elementCount = m + n

        for currentPos in reversed(range(elementCount)):
            # Nothing left in the second list
            if (rightPos < 0):
                break
            # Move an element from second list to first list if it is larger OR
            # we only have 2nd list
            elif (leftPos < 0) or nums1[leftPos] < nums2[rightPos]:
                nums1[currentPos] = nums2[rightPos]
                rightPos -= 1
            # Advance the first list if it is larger
            else:
                nums1[currentPos] = nums1[leftPos]
                leftPos -= 1

