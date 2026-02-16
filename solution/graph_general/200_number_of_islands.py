from itertools import product
from typing import List

class Solution:
    def getNeighbors(self, remaining: set(tuple(int)), point: tuple(int)) -> list(tuple(int)):
        r""" Generates the 4 valid points and checks which ones can be 'visited'
        and return it back.
        """

        x, y = point
        possibleSet = set(((x-1, y), (x+1, y), (x, y-1), (x, y+1)))
        validOptions = remaining & possibleSet

        remaining -= validOptions
        possibleSet -= validOptions

        return list(validOptions)

    def getAll1(self, grid: List[List[str]]) -> set(tuple(int)):
        r""" This scans for all valid points (i.e. land which is marked as '1')
        and makes a proper set of all of them.
        """

        #(((m, n) for n, value in enumerate(row) if value != '0') for m, row in enumerate(grid))
        ret = set()
        for m, row in enumerate(grid):
            ret.update((m, n) for n, value in enumerate(row) if value != '0')
        return ret

    def numIslands(self, grid: List[List[str]]) -> int:

        islandCount = 0
        allPoints = self.getAll1(grid)

        while allPoints:
            newPoint = allPoints.pop()
            #print(f"New island with {newPoint=}")
            currentPoints = [newPoint]

            # Scan all of Current Island
            while currentPoints:
                currentPoint = currentPoints.pop()
                validPoints = self.getNeighbors(allPoints, currentPoint)
                if validPoints:
                    #print(f"Adding new points {validPoints=}")
                    pass
                currentPoints.extend(validPoints)
            islandCount += 1
        return islandCount


if __name__ == '__main__':
    solution = Solution()
    grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
    finalIslandCount = solution.numIslands(grid)
    print(finalIslandCount)

