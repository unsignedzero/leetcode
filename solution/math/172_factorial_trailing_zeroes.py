from math import log, sqrt

class Solution:
    def trailingZeroes(self, n: int) -> int:

        if n < 5:
            return 0

        fiveCount, zeroCount = 5, 0
        k = int(log(n, 5)) # Check for how many powers of 5 we may have

        for _ in range(k):
            count = n // fiveCount
            zeroCount += count
            fiveCount *= 5

        return zeroCount

    def otherCode(self, n: int) -> int:
        r""" Attempt to divide by 5 and count those.
        """

        count = 0

        while (n > 0) :
            n //= 5
            count += n
        return count

    def oldCode(self, n: int) -> int:
        r""" The first solution where we just keep track of number that are
        divisible by 5. Each 5 is one zero as we have more 2s than 5s.
        """

        count = 0

        for i in range(1, n + 1):
            while True:
                if i % 5 == 0:
                    count +=1
                    i /= 5
                else:
                    break

        return count

