from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r"""We have an ordered int list and want to find a value if it
        exists as a sum of two values. We just need to have a 'pointer'
        on both sides and iterate until exists!
        """

        left, right = 0, len(numbers) - 1

        while left < right:
            result = numbers[left] + numbers[right]

            # Select which pointer to move as needed.
            if result > target:
                right -= 1
            elif result < target:
                left += 1
            else:
                return [left + 1, right + 1]

        return []

if __name__ == '__main__':
    solution = Solution()
