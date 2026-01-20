from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        r""" For this we keep track of the left and right side and keep track
        of each step and amount of water we can add.
        """

        leftPos, rightPos = 0, len(height) - 1
        leftMax = rightMax = 0
        rainWater = 0

        while (leftPos <= rightPos):

            if (leftMax <= rightMax) :
                leftMax = max(leftMax, height[leftPos])
                rainWater += leftMax - height[leftPos]
                leftPos += 1

            else:
                rightMax = max(rightMax, height[rightPos])
                rainWater += rightMax - height[rightPos]
                rightPos -= 1

        return rainWater

