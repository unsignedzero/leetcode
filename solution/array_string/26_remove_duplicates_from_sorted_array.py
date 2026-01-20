from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        r""" We just need to care about increasing elements and ignore the
        rest of the array. We can use the duplicate count to get the right index.
        """

        duplicateCount = 0
        currentValue = float('-inf')

        for index in range(len(nums)):
            # Write the value if it is increasing
            if currentValue < nums[index]:
                currentValue = nums[index]
                nums[duplicateCount] = nums[index]
                duplicateCount += 1

        return duplicateCount

