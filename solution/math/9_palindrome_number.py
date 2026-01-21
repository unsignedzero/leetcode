class Solution:
    def isPalindrome(self, x: int) -> bool:
        intString = str(x)
        digitCount = len(intString)

        for index in range(digitCount//2):
            if intString[index] != intString[digitCount - index - 1]:
                return False
        return True

