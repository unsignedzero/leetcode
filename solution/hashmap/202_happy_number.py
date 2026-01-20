from typing import List

class Solution:
    def convertIntToDigit(self, n: int) -> list[int]:
        return [int(d) for d in str(n)]

    def process(self, ints: list[int]) -> int:
        return sum(x * x for x in ints)

    def isHappy(self, n: int) -> bool:
        seen = set()
        lastValue = n

        while lastValue not in seen:
            seen.add(lastValue)
            nextValue = self.process(self.convertIntToDigit(lastValue))
            if nextValue == 1 or nextValue == 7:
                return True

            lastValue = nextValue

        return False

if __name__ == '__main__':
    a = Solution()
    print(a.isHappy(19))

