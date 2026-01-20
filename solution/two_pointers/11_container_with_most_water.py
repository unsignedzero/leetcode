from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        r""" Working solution for figuring out the max amount of water
        between two columns.
        """

        left, right = 0, len(height) - 1
        bestSum = 0

        while left < right:
            bestSum = max(bestSum, min(height[left], height[right]) * (right - left))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return bestSum

    def maxArea2(self, height: List[int]) -> int:
        r""" First guess of the solution messing up when to move left or right.
        """

        left, right = 0, len(height) - 1
        bestSum = 0

        while left < right:
            bestSum = max(bestSum, min(height[left], height[right]) * (right - left))

            if height[right - 1] > height[right]:
                right -= 1
            elif height[left + 1] > height[left]:
                left += 1
            else:
                left += 1

        return bestSum

if __name__ == '__main__':
    solution = Solution()
