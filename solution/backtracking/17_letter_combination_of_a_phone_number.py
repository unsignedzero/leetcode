from typing import List

DIGITS_MAPPING = {2: 'abc',
                  3: 'def',
                  4: 'ghi',
                  5: 'jkl',
                  6: 'mno',
                  7: 'pqrs',
                  8: 'tuv',
                  9: 'wxyz'
                 }

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        r""" We process in reverse from the bottom so the final string we build
        is ordered correctly.
        """
        result = []

        # Process in reserve
        for digit in digits[::-1]:
            if not result:
                result = list(DIGITS_MAPPING[int(digit)])
            else:

                newResult = []

                for eachLetter in DIGITS_MAPPING[int(digit)]:
                    newResult.extend([f"{eachLetter}{x}" for x in result])
                result = newResult

        return result

