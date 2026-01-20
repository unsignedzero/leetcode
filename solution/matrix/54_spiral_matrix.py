from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r"""For this solution, we move the edge in one side at a time.

        My original solution that was lost was basically using an alternative sequence
        to get the right column/row but it has many edge cases.
        The idea was that for say a 5x5
        you would generate a pattern [1,5,2,4,3] and iterate on the sides.
        """

        rows, cols = len(matrix), len(matrix[0])
        left, top = 0, 0
        right, bottom = cols - 1, rows - 1
        result = []

        while top <= bottom and left <= right:
            # Top Row
            result.extend(matrix[top][index] for index in range(left, right+1))
            top +=1

            # Right Column
            result.extend(matrix[index][right] for index in range(top, bottom+1))
            right -=1

            if top <= bottom:
                # Bottom Row
                result.extend(matrix[bottom][index] for index in range(right, left-1, -1))
                bottom -= 1

            if left <= right:
                # Left Column
                result.extend(matrix[index][left] for index in range(bottom, top-1, -1))
                left += 1

        return result

