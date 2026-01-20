from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r""" Checks if a Sudoku puzzle is valid by checking:
        * All numbers in the row is unique
        * All numbers in the column is unique
        * All numbers in the group are unique.

        We can optimize further by caching intermediate results but that wastes space.
        We can make 3 boolean tables:
            [row][number]
            [column][number]
            [column * 3 + row][number]
        and set if them to be True. If we see an already True value, then we are duplicating.
        """

        self.board = board
        for x, row in enumerate(board):
            for y, value in enumerate(row):
                if value != ".":
                    a = self.isRowValid(x, y, value)
                    b = self.isColumnValid(x, y, value)
                    c = self.isGroupValid(x, y, value)
                    if not all([a, b, c]):
                        return False
        return True

    def isRowValid(self, col: int, row: int, value: str) -> bool:
        # We can optimize this to be one list comprehension.
        count = 0
        for val in range(9):
            if self.board[col][val] == value:
                count += 1
        return count <= 1

    def isColumnValid(self, col: int, row: int, value: str) -> bool:
        # We can optimize this to be one list comprehension.
        count = 0
        for val in range(9):
            if self.board[val][row] == value:
                count += 1
        return count <= 1

    def isGroupValid(self, col: int, row: int, value: str) -> bool:
        count = 0
        topX, topY = col // 3, row // 3

        # We can optimize it down to one for loop.
        for x in range(3):
            for y in range(3):
                if self.board[topX * 3 + x][topY * 3 + y] == value:
                    count += 1
        return count <= 1
