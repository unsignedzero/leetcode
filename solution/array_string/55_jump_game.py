from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        r"""We do a one sweep calculating if we can make it by checking
        if we have more jumpvalues as a option. We don't keep track of the path
        just if it is possible.
        """

        jumpDistanceLeft = 0

        for jumpGain in nums:

            if jumpDistanceLeft < 0:
                return False
            elif jumpGain > jumpDistanceLeft:
                jumpDistanceLeft = jumpGain

            jumpDistanceLeft -= 1
        return True

    def canJump2(self, nums: List[int]) -> bool:
        r"""A brute-force recursive approach to see if we can make it by
        checking all possible values.
        """

        if len(nums) <= 1:
            return True
        elif nums[0] == 0:
            return False

        return any(self.canJump2(nums[i:]) for i in range(1, nums[0] + 1))

