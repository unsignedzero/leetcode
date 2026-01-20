from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        r""" Since there is a majority, >= n/2 times, of one element, we can assume that
        we just count the current highest one and decrement for any that doesn't
        match and we will find the majority element.

        For general purpose, we can use collections.Counter to get the frequency of all elements.
        """

        currentValue, currentValueCount = nums[0], 0

        for value in nums:
            if currentValue == value:
                currentValueCount += 1
            else:
                currentValueCount -= 1

            if currentValueCount == 0:
                currentValueCount = 1
                currentValue = value

        return currentValue

