from typing import List
from copy import deepcopy

class Solution:
    def totalNQueens(self, n: int) -> int:
        r""" A brute force solution placing queens in the first available spot.
        We can likely use bits to store the board to reduce size and make copying
        faster
        """

        queenCount = 0

        def advanceBoard(height: int, currentBoard: List[List[str]]):

            for x in range(n):
                #print(f"height: {height}, x: {x}, state {currentBoard}")
                if currentBoard[height][x] == '_':
                    if height == n - 1:
                        nonlocal queenCount
                        queenCount += 1
                        break

                    # We need a full deep copy of the board, else we only copy references
                    newBoard = deepcopy(currentBoard)

                    # Fill row
                    for i in range(n):
                        newBoard[height][i] = 'r'

                    # Fill column. We don't need to fill the top section since we are
                    # scanning down
                    for i in range(height, n):
                        newBoard[i][x] = 'c'

                    # Diagonals
                    # Likely can be optimized
                    for i in range(-n + 1, n):
                        if 0 <= height + i < n and 0 <= x + i < n:
                            #print(f"({height + i}, {x + i})")
                            newBoard[height + i][x + i] = 'd'
                        if 0 <= height + i < n and 0 <= x - i < n:
                            #print(f"({height + i}, {x - i})")
                            newBoard[height + i][x - i] = 'd'

                    newBoard[height][x] = 'q'
                    # Pass to next area
                    advanceBoard(height + 1, newBoard)

        BLANK_BOARD = []
        for _ in range(n):
            BLANK_BOARD.append(['_'] * n)

        advanceBoard(0, BLANK_BOARD)

        return queenCount

if __name__ == '__main__':
    solution = Solution()
    print(solution.totalNQueens(4))

