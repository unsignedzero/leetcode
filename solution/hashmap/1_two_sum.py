from collections import defaultdict
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        r""" Sort the input string and find the right right two elements
        that add up to a certain int value.
        """

        left, right = 0, len(nums) - 1

        mapping = defaultdict(list)

        for index, element in enumerate(nums):
            mapping[element].append(index)

        nums.sort()

        while left < right:
            currentSum = nums[left] + nums[right]
            if currentSum == target:
                # Get two elements
                if nums[left] == nums[right]:
                    return (mapping[nums[left]][0], mapping[nums[right]][1])
                else:
                    return (mapping[nums[left]][0], mapping[nums[right]][0])

            elif currentSum > target:
                right -= 1
            elif currentSum < target:
                left += 1

        return ()

