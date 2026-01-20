class Solution:
    def isPalindrome(self, s: str) -> bool:
        r"""We need to sanitize the input by removing non-alphanumeric
        and matching lower casing before doing a check.
        """

        newString = "".join(c.lower() for c in s if c.isalnum())
        lastPos = len(newString) - 1

        # We only need to iterate for half of these and stop at the mid point
        for pivot in range(lastPos // 2 + 1):
            if newString[pivot] != newString[lastPos - pivot]:
                return False
        return True

if __name__ == '__main__':
    solution = Solution()
