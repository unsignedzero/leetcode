from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        r""" We opt to use the two pointer solution moving the start and end
        together to the right spot.
        """

        start, end = 0, 1
        minLength = float('inf')
        currentSum = nums[0]

        while True:

            if currentSum < target:
                end += 1
                if end > len(nums):
                    break
                currentSum += nums[end - 1]

            else:
                length = end - start

                if length < minLength:
                    minLength = length

                start += 1
                currentSum -= nums[start - 1]

        if minLength < float('inf'):
            return minLength
        else:
            return 0

    def minSubArrayLen2(self, target: int, nums: List[int]) -> int:
        r""" Brute force solution trying to find the min size of the sub array
        """
        minSize = float('inf')

        for startIndex, val in enumerate(nums):
            tempSum = val

            if tempSum >= target:
                 return 1

            for otherIndex, otherVal in enumerate(nums[startIndex+1:], startIndex+1):

                tempSum += otherVal

                if tempSum >= target:
                    currentLength = otherIndex - startIndex + 1
                    if currentLength < minSize:
                        minSize = currentLength
                    break

        if minSize == float('inf'):
            return 0
        else:
            return minSize

if __name__ == '__main__':
    solution = Solution()
