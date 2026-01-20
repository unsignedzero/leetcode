from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        r""" We need to move up elements we removed and report the count back.
        """

        countOfNumbersRemoved = 0

        for index in range(len(nums)):
            if nums[index] != val:
                nums[countOfNumbersRemoved] = nums[index]
                countOfNumbersRemoved += 1

        return countOfNumbersRemoved

