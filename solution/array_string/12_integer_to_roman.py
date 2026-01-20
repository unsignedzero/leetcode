class Solution:
    def intToRoman(self, num: int) -> str:
        r""" Here we convert each position in the number into it's roman numeral
        counterpart and concatenate the string back together.
        """
        romanValue =   {1: 'I',
                        5: 'V',
                        10: 'X',
                        50: 'L',
                        100: 'C',
                        500: 'D',
                        1000: 'M'}
        deltaMapping = {4: 'IV',
                        9: 'IX',
                        40: 'XL',
                        90: 'XC',
                        400: 'CD',
                        900: 'CM'}

        resultString = []

        for position in (1000, 100, 10, 1):
            value = num // position

            # We only want the 'last' digit in the number
            if value >= 10:
                value = value % 10

            # Catch the special cases here
            if value == 9 or value == 4:
                resultString.append(deltaMapping[value * position])
                continue
            elif value >= 5:
                value -= 5
                resultString.append(romanValue[5 * position])

            # Get the remaining value
            if value:
                resultString.append(value * romanValue[position])

        return "".join(resultString)
