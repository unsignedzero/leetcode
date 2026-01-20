from collections import defaultdict

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        r""" Check if there's a mapping so that all char in s can be mapped into t and vice versa.
        """

        if len(s) != len(t):
            return False

        leftDict, rightDict = dict(), dict()

        for index in range(len(s)):
            leftLetter, rightLetter = s[index], t[index]
            if leftLetter not in leftDict:
                leftDict[leftLetter] = rightLetter
            if rightLetter not in rightDict:
                rightDict[rightLetter] = leftLetter

            if leftDict[leftLetter] != rightLetter or rightDict[rightLetter] != leftLetter:
                return False
        return True

