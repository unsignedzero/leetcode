class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        r"""We need to check string s is a substring in t.
        """

        endIndex = len(s)

        # If s is empty, this is trivially true
        if endIndex == 0:
            return True
        # If t is empty, this is trivially false
        elif len(t) == 0:
            return False

        nextIndex = 0
        currentChar = s[nextIndex]

        for eachChar in t:
            # If we mind a match, update the s position and continue until we hit the end.
            if currentChar == eachChar:
                nextIndex += 1
                if nextIndex == endIndex:
                    return True
                currentChar = s[nextIndex]

        return False

if __name__ == '__main__':
    solution = Solution()
