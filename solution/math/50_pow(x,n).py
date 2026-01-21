class Solution:
    def myPow(self, x: float, n: int) -> float:
        r""" A nicer variant of my solution which uses the stack to process the powers
        as needed.
        """

        if n == 0:
            return 1
        if n < 0:
            return 1/self.myPow(x, -n)

        if n%2 == 0:
            return self.myPow(x*x, n//2)
        else:
            return x * self.myPow(x, n-1)

    def myPow2(self, x: float, n: int) -> float:
        r""" A more optimized solution in which we stack the powers in a binary
        fashion and then multiple what we need together.
        """

        if n == 0:
            return 1
        if n<0:
            return 1/self.myPow(x, -n)

        resultList = [x]

        result = 1
        while n > 0:
            if n & 1:
                result *= resultList[-1]
            resultList.append(resultList[-1] * resultList[-1])
            n>>=1

        return result

    def myPow3(self, x: float, n: int) -> float:
        r""" My original solution that brute forces the solution by
        multiplying the value out.
        """

        result = 1
        negative = n < 0

        if n < 0:
            n = -n

        for _ in range(n):
            result *= x

        return 1/result if negative else result

