class Solution:
    def addBinary(self, a: str, b: str) -> str:
        lenA, lenB = len(a), len(b)
        reversedResult = []

        # Pad the strings so they are equal length
        if lenA != lenB:
            delta = lenA - lenB
            if delta > 0:
                b = ('0' * delta) + b
            else:
                a = ('0' * (-delta)) + a

        carry = 0
        for leftBit, rightbit in zip(a[::-1], b[::-1]):
            result = int(leftBit) + int(rightbit) + carry
            if result >= 2:
                carry = 1
                result -= 2
            else:
                carry = 0
            reversedResult.append(str(result))
        if carry:
            reversedResult.append("1")

        return "".join(reversedResult[::-1])

if __name__ == '__main__':
    a = Solution()
    print(a.addBinary('101', '10'))

