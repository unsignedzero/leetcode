class Solution:
    def mySqrt(self, x: int) -> int:
        r""" The solution is a binary search for the right square root.
        """

        if x == 0:
            return 0

        left, right, ans = 1, x, 0

        while left <= right:
            mid = left + (right - left) // 2
            square = mid * mid

            if square == x:
                return mid

            elif square < x:
                ans = mid
                left = mid + 1

            elif square > x:
                right = mid - 1

        return ans

