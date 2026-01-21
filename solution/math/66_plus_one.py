from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        rightIndex = len(digits) - 1
        finalCarry = False

        for index in range(rightIndex, -1, -1):
            value = digits[index] + 1

            if value < 10:
                digits[index] = value
                finalCarry = False
                break

            digits[index] = 0
            finalCarry = True

        if finalCarry:
            digits.insert(0, 1)

        return digits

