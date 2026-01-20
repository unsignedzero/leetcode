class Solution:
    def romanToInt(self, s: str) -> int:
        r""" We lean on maps to store the state of the values
        """

        romanValue = {'I': 1,
                      'V': 5,
                      'X': 10,
                      'L': 50,
                      'C': 100,
                      'D': 500,
                      'M': 1000}
        deltaMapping = {('I', 'V'): 4,
                        ('I', 'X'): 9,
                        ('X', 'L'): 40,
                        ('X', 'C'): 90,
                        ('C', 'D'): 400,
                        ('C', 'M'): 900,
                       }

        lastChar = None
        finalSum = 0

        for letter in s:
            pair = (lastChar, letter)

            # Readjust if we realize it's a special pair
            if pair in deltaMapping:
                finalSum = finalSum - romanValue[lastChar] + deltaMapping[pair]
            else:
                finalSum += romanValue[letter]
            lastChar = letter

        return finalSum

if __name__ == '__main__':
    solution = Solution()
    print(solution.romanToInt("MCMXCIV"))
