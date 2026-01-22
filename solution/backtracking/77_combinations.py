from typing import List
from itertools import combinations

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        r""" Use stdlib tools
        """
        return list(combinations(range(1, n+1), k))

    def combine2(self, n: int, k: int) -> List[List[int]]:
        r""" We iterate and add any element we are not missing.
        """
        possibleValues = list(range(1, n+1))

        # Empty case
        if k > n or k == 0:
            return [[]]

        # Solve k = 1
        result = []
        for i in range(n):
            result.append([i])

        if k == 1:
            return result

        # Solve k > 1
        for _ in range(2, k + 1):
            newResult = []

            # Group to add
            tempResult = result.copy()
            for eachElement in tempResult:

                # Element to add
                for i in range(1, n+1):
                    if i not in eachElement:
                        eachElement.append(i)
                        newResult.append(sorted(eachElement))

            result = newResult

        return result
