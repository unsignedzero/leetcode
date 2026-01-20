from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        r""" For this we generate the pre/post fix values and update the
        solution list and return it back.
        """

        numsLength = len(nums)
        solutionList = [1] * numsLength
        prefixProduct = postfixProduct = 1

        # Interestingly enough using enumerate and zip is slower than
        # just range and accessing the n-th index on nums
        for leftIndex in range(numsLength):
            rightIndex = numsLength - leftIndex - 1

            solutionList[leftIndex] *= prefixProduct
            prefixProduct *= nums[leftIndex]

            solutionList[rightIndex] *= postfixProduct
            postfixProduct *= nums[rightIndex]

        return solutionList

