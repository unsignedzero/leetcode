from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        r""" We need to move up elements we removed and report the count back.
        """

        countOfNumbersRemoved = 0

        for index in range(len(nums)):
            if nums[index] != val:
                nums[countOfNumbersRemoved] = nums[index]
                countOfNumbersRemoved += 1

        return countOfNumbersRemoved

if __name__ == '__main__':
    solution = Solution()
    nums1 = [0,1,2,2,3,0,4,2]
    val = solution.removeElement(nums1, 2)
    print(f"list: {nums1}: removed: {val}")

