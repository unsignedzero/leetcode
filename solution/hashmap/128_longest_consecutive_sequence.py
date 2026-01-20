from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        r""" The third solution. This tracks edges instead of values so it
        is faster on larger values.
        """

        setNumber = set(nums)
        table = {}
        longestStreak = 0

        for number in setNumber:
            x = table.get(number - 1, 0)
            y = table.get(number + 1, 0)
            #print(f"number:{number}, x:{x}, y:{y}, table:{table}")
            currentStreak = x + y + 1
            #print(f"Updating: {number - x}, {number - y} with {currentStreak}")
            table[number - x] = currentStreak
            table[number + y] = currentStreak

            longestStreak = max(longestStreak, currentStreak)

        return longestStreak

    def longestConsecutive2(self, nums: List[int]) -> int:
        r""" A faster set based solution. It is also too slow.
        """

        seen = set(nums)
        longestStreak = 0

        for number in nums:
            if number-1 not in seen:
                currentStreak = 1
                nextNumber = number + 1
                while nextNumber in seen:
                    nextNumber += 1
                    currentStreak += 1
                longestStreak = max(longestStreak, currentStreak)

        return longestStreak

    def longestConsecutive3(self, nums: List[int]) -> int:
        r""" My first solution. It is a slow brute force solution.
        """

        if not nums:
            return 0

        seen = dict()

        for number in nums:

            if number-1 in seen:
                seen[number] = seen[number - 1] + 1
            else:
                seen[number] = 1

            index = number + 1
            while index in seen:
                seen[index] = seen[index - 1] + 1
                index += 1

        return max(seen.values())

if __name__ == '__main__':
    solution = Solution()
    print(solution.longestConsecutive([100,4,200,1,3,2]))
    print(solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))

