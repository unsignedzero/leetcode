from typing import List

class Solution:
    def getNeighbors(self, point: tuple(int), maxPoint: tuple(int)) -> list(tuple(int)):
        r""" Generates the 4 valid points and checks which ones can be 'visited'
        and return it back.
        """

        maxy, maxx = maxPoint
        y, x = point
        possibleSet = set(((y-1, x), (y+1, x), (y, x-1), (y, x+1)))
        validOptions = filter(lambda pt : 0 <= pt[0] <= maxy and 0<= pt[1] <= maxx, possibleSet)

        return list(validOptions)

    def getAllEdges(self, board: List[List[str]]) -> set(tuple(int)):
        r""" Get all points on any edge of the board.
        """

        heightCount = len(board)
        rowCount = len(board[0])

        returnSet = set()

        returnSet.update((y, 0) for y in range(heightCount))
        returnSet.update((0, x) for x in range(rowCount))
        returnSet.update((y, rowCount-1) for y in range(heightCount))
        returnSet.update((heightCount-1, x) for x in range(rowCount))

        return returnSet

    def finalizeBoard(self, board: List[List[str]]) -> None:
        r""" All valid points that touch the edge are '0'. We change that back
        to 'O' and all 'O' are 'X' since they don't share an edge with the side of the board.
        """

        for y, row in enumerate(board):
            for x, value in enumerate(row):
                if value == '0':
                    board[y][x] = 'O'
                elif value == 'O':
                    board[y][x] = 'X'


    def solve(self, board: List[List[str]]) -> None:

        allEdgePoints = self.getAllEdges(board)
        LARGEST_POINT = max(allEdgePoints)
        #print(allEdgePoints)

        while allEdgePoints:
            newPoint = allEdgePoints.pop()
            currentPoints = [newPoint]
            while currentPoints:
                y, x = currentPoint = currentPoints.pop()
                #print(f"({y}, {x})")
                if board[y][x] == 'O':
                    #print(f"({y}, {x}) is O")
                    board[y][x] = '0'
                    validPoints = self.getNeighbors(currentPoint, LARGEST_POINT)
                    currentPoints.extend(validPoints)

        self.finalizeBoard(board)

if __name__ == '__main__':
    solution = Solution()
    board = [
  ["O","O","O","O","X"],
  ["O","O","X","O","X"],
  ["O","O","X","X","X"],
  ["X","X","X","X","X"]
]
    board = [
  ["X","X","X","X","X"],
  ["X","O","O","X","X"],
  ["X","X","O","X","X"],
  ["X","O","X","X","X"]
]
    solution.solve(board)
    print(board)

