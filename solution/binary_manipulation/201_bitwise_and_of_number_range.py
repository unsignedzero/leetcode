class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        r""" A more optimized solution finding the common prefix on the ints that
        exist.
        """

        shift = 0
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift

    def rangeBitwiseAnd2(self, left: int, right: int) -> int:
        r""" My first solution that takes too much time to run but is a
        simple brute force solution
        """

        result = left

        for i in range(left, right + 1):
            result &= i
            if result == 0:
                return 0

        return result

