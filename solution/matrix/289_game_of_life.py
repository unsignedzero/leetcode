from typing import List

class Solution:
    def getNeighborCount(self, x: int, y: int, lenX: int, lenY: int, board: List[List[int]]) -> int:
        r""" Get the count of all neighbors
        """

        count = 0

        # A wacky for loop so we can always be in bounds.
        for i in range(max(0, x - 1), min(lenX, x + 2)):
            for j in range(max(0, y - 1), min(lenY, y + 2)):
                #print(f"({j}, {i} : {board[j][i]})")
                count += board[j][i]

        # We are counting itself which we need to remove
        return count - board[y][x]

    def applyRule(self, oldState: int, count: int) -> int:
        r""" Apply the game of life rules here
        """

        if oldState == 1:
            if 2 <= count <= 3:
                return 1
            else:
                return 0

        elif count == 3:
            return 1
        return 0

    def gameOfLife(self, board: List[List[int]]) -> None:
        r""" Top level calling class
        """

        lenX = len(board[0])
        lenY = len(board)

        # Initialize the new board
        newBoard = []
        for _ in range(lenY):
            newBoard.append(lenX * [0])

        # Apply the rules to the new board
        for y in range(lenY):
            for x in range(lenX):
                count = self.getNeighborCount(x, y, lenX, lenY, board)
                newBoard[y][x] = self.applyRule(board[y][x], count)

        # Copy the new board back to the old board
        for y in range(lenY):
            for x in range(lenX):
                board[y][x] = newBoard[y][x]

if __name__ == '__main__':
    solution = Solution()
    board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    solution.gameOfLife(board)
    print(board)

