from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        r""" This is my first solution where store the zeroes in a separate
        list and apply it as needed. This makes the code easy to read.
        """

        columnSize, rowSize = len(matrix), len(matrix[0])
        zeroes = []

        # Find zeroes
        for x in range(rowSize):
            for y in range(columnSize):
                if matrix[y][x] == 0:
                    zeroes.append((x, y))

        # Apply zeroes
        for x, y in zeroes:
            for i in range(rowSize):
                matrix[y][i] = 0
            for j in range(columnSize):
                matrix[j][x] = 0

    def setZeroes2(self, matrix: List[List[int]]) -> None:
        r""" This is a space-optimized solution where we use the 0-row/0-column
        to store value versus have something else to store the 0 we spot.

        The working copy somehow didn't get saved so this doesn't work in all cases.
        """

        columnSize, rowSize = len(matrix), len(matrix[0])
        #print(matrix)

        # We find the initial zero
        for x in range(rowSize):
            for y in range(columnSize):
                if matrix[y][x] == 0:
                    matrix[y][0] = 0
                    matrix[0][x] = 0
        #print(matrix)

        # We apply 0 by column
        for i in range(1, rowSize):
            if matrix[0][i] == 0:
                #print(f"Found zero at (0, {i})")
                for j in range(1, columnSize):
                    matrix[j][i] = 0
        #print(matrix)

        # We apply 0 by row
        for j in range(1, columnSize):
            if matrix[j][0] == 0:
                #print(f"Found zero at ({j}, 0)")
                for i in range(1, rowSize):
                    matrix[j][i] = 0
        #print(matrix)

        # We apply the last top/left zero
        if matrix[0][0] == 0:
            for i in range(rowSize):
                matrix[0][i] = 0
            for j in range(columnSize):
                matrix[j][0] = 0

if __name__ == '__main__':
    solution = Solution()
    inputMatrix = [[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]
    solution.setZeroes(inputMatrix)
    print(inputMatrix)

