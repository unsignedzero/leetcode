class Solution:
    r""" My original solution did not work fully after debugging for awhile
    35/49 cases passed
    """

    def tokenizeInput(self, s: str) -> list:
        storage = []
        currentInt = []

        for eachChar in s:
            if eachChar not in ('+', '-', '(', ')', ' '):
                currentInt.append(eachChar)
            elif eachChar != ' ':
                if currentInt:
                    storage.append(int("".join(currentInt)))
                storage.append(eachChar)
                currentInt = []

        if currentInt:
            storage.append(int("".join(currentInt)))

        return storage

    def processTokens(self, subExpression: list) -> int:
        seen = []
        isNegativeNumber = False

        for element in subExpression:
            if element == '-':
                if not seen or not isinstance(seen[-1], int):
                    isNegativeNumber = True
                    continue
                else:
                    seen.append(element)
            elif element == '+':
                seen.append(element)
            else:
                if isNegativeNumber:
                    seen.append(-element)
                    isNegativeNumber = False
                else:
                    seen.append(element)

            if len(seen) == 3:
                right = seen.pop()
                operator = seen.pop()
                left = seen.pop()
                if operator == '+':
                    seen.append(left + right)
                else:
                    seen.append(left - right)
        return seen.pop()

    def flatten(self, l: list[list]) -> list:
        finalList = []
        if not isinstance(l, list):
            return l
        for element in l:
            if not isinstance(l, list):
                finalList.append(element)
            else:
                result = (self.flatten(element))
                if isinstance(result, list):
                    finalList.extend(result)
                else:
                    finalList.append(result)

        return finalList

    def calculate(self, s: str) -> int:

        # Internalize string
        storage = self.tokenizeInput(s)

        currentStack = []
        currentBuffer = []

        print(f"storage: {storage}")
        for eachElement in storage:
            print(f"currentStack: {currentStack}, currentBuffer: {currentBuffer}, eachElement: {eachElement}")
            if eachElement == '(':
                currentStack.append(currentBuffer)
                currentBuffer = []

            elif eachElement == ')':
                # process values and pop '(' Storage on stack
                if len(currentBuffer) == 1:
                    tempBuff = currentStack.pop()
                    tempBuff.extend(currentBuffer)
                    currentBuffer = tempBuff
                value = self.processTokens(currentBuffer)
                currentBuffer = []
                currentBuffer.append(value)
            else:
                currentBuffer.append(eachElement)

        currentStack.extend(currentBuffer)
        return self.processTokens(self.flatten(currentStack))

