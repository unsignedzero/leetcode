from typing import List

class Solution:
    def reverse(self, left, right):
        r""" This swaps elements pairs from left to right to reverse the
        segment of the list.
        """

        while left < right:
            self.nums[left], self.nums[right] = self.nums[right], self.nums[left]
            left += 1
            right -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        r""" The more optimal solution is just 3 reversals.
        1. Reverse from 0 -> n-k-1
        2. Reverse from n-k -> n-1
        3. Reverse the full array from 0 -> n
        """

        # Rather than passing it around, we can store it in the class.
        self.nums = nums

        lenNums = len(nums)
        # We only need to rotate at most k-1 times. We can reduce that down
        k %= lenNums

        self.reverse(0, lenNums - 1)
        self.reverse(0, k - 1)
        self.reverse(k, lenNums - 1)

    def rotate2(self, nums: List[int], k: int) -> None:
        r"""This is the less optimal solution as we generate a new "rotation"
        and need to store it back to the original list.
        """

        lenNums = len(nums)

        # We only need to rotate at most k-1 times. We can reduce that down
        if k >= lenNums:
            k = k % lenNums
        # No need to rotate if it is zero
        if k == 0:
            return nums

        # Get the index of where the new first value is
        remains = lenNums - k

        # We construct a new array. We can rotate in place but this is the first ieration
        new = nums[remains:remains + k] + nums[:remains]
        for index, val in enumerate(new):
            nums[index] = val

