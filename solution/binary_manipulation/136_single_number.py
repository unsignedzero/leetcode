from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        r"""There is a number of integers passed in such that all are
        passed as pairs but only one is passed as a single. We need to find that
        one unique one. A map is obvious and then find the odd one but we can use
        XOR.
        """

        number = 0
        for currentNumber in nums:
            number = number ^ currentNumber
        return number

