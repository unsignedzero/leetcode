from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        r"""This changes the earlier #26 problem that allows up to two
        elements of the same value. We just need to add in another case for this.
        """

        duplicateCount = seenCount = 0
        lowValue = float('-inf')

        for index in range(len(nums)):
            if lowValue < nums[index]:
                lowValue = nums[index]
                nums[duplicateCount] = nums[index]
                duplicateCount += 1
                seenCount = 1
            elif lowValue == nums[index] and seenCount == 1:
                nums[duplicateCount] = nums[index]
                duplicateCount += 1
                seenCount += 1
            # This will ignore all we've seen more than twice
            # else:

        return duplicateCount

