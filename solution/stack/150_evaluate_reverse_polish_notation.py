class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        internalStack = []

        for eachElement in tokens:
            if eachElement not in ("+", "-", "*", "/"):
                internalStack.append(int(eachElement))

            elif eachElement == "+":
                value = internalStack.pop() + internalStack.pop()
                internalStack.append(value)
            elif eachElement == "-":
                top = internalStack.pop()
                bottom = internalStack.pop()
                value = bottom - top
                internalStack.append(value)

            elif eachElement == "*":
                value = internalStack.pop() * internalStack.pop()
                internalStack.append(value)
            elif eachElement == "/":
                top = internalStack.pop()
                bottom = internalStack.pop()
                value = int(bottom / top)
                internalStack.append(value)

        return internalStack.pop()
