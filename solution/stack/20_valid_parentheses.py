class Solution:
    def isValid(self, s: str) -> bool:
        r""" Small optimization using a map to check the pair if they match
        """

        bracketMap = {'(':')', '{':'}', '[':']'}
        stack = []
        for eachChar in s:

            if eachChar in bracketMap:
                stack.append(eachChar)
            elif len(stack) == 0 or bracketMap[stack.pop()] != eachChar:
                return False

        return len(stack) == 0

    def isValid2(self, s: str) -> bool:

        r""" First solution embedding the chars in the code itself.
        """

        stack = []
        for eachChar in s:

            if eachChar in "([{":
                stack.append(eachChar)
            else:
                try:
                    stackChar = stack.pop()
                    if ((stackChar == '[' and eachChar == ']') or
                        (stackChar == '(' and eachChar == ')') or
                        (stackChar == '{' and eachChar == '}')):
                        pass
                    else:
                        return False
                except IndexError:
                    return False

        return len(stack) == 0

