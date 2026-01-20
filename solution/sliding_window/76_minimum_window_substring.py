from typing import List
from collections import Counter

class Solution:
    def updateBestMatch(self, newValue: List[int]) -> None:
        if self.bestMatch:
            if (newValue[1] - newValue[0]) < (self.bestMatch[1] - self.bestMatch[0]):
                self.bestMatch = newValue
        else:
            self.bestMatch = newValue

    def minWindow(self, s: str, t: str) -> str:
        r""" A slow but workable solution where we move two pointers forward
        and try to find the shortest string contains that has all letters from t.
        """


        lenS, lenT = len(s), len(t)
        # Check impossible case
        if lenT > lenS:
            return ""

        # We use counters to check if the string contained between left/right
        # has all letters of t
        residual = Counter(t)
        current = Counter()

        leftPos, rightPos = 0, 0
        self.bestMatch = None

        while True:
            #print(f">>>Current Loop: leftPos {leftPos}")

            # Advance right until we can match
            while rightPos < lenS:

                newChar = s[rightPos]
                current[newChar] += 1
                rightPos += 1
                #print(f"Advancing right {rightPos}")

                if current >= residual:
                    #print(f"Right Updating interval to ({leftPos}, {rightPos})")
                    nextMatch = [leftPos, rightPos]
                    self.updateBestMatch(nextMatch)
                    break

            # Move left up until we cannot match
            while current >= residual:
                #print(f"Comparison {current} >= {residual}")
                #print(f"Left Updating interval to ({leftPos}, {rightPos})")
                nextMatch = [leftPos, rightPos]
                self.updateBestMatch(nextMatch)

                newChar = s[leftPos]
                current[newChar] -= 1
                leftPos += 1
                #print(f"Advancing left {leftPos}")
            # If there was never a match, we just advance left
            else:
                if (leftPos + lenT) < lenS:
                    newChar = s[leftPos]
                    current[newChar] -= 1
                    leftPos += 1
                    #print(f"Advancing left {leftPos}")
                else:
                    break

        if self.bestMatch:
            return s[self.bestMatch[0]:self.bestMatch[1]]
        else:
            return ""

if __name__ == '__main__':
    solution = Solution()
    #print(solution.minWindow("ADOBECODEBANC", "ABC"))
    #print(solution.minWindow("cabeca", "cae"))
    #print(solution.minWindow("bdab", "ab"))
    print(solution.minWindow("abc", "cba"))
    #print(solution.minWindow("ab", "a"))
    #print(solution.minWindow("a", "a"))
