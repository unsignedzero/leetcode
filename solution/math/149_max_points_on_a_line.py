from collections import defaultdict
from itertools import permutations
from operator import itemgetter
from typing import List

class Solution:

    def calculateBestFitLine(self, points: List[List[int]]) -> List[int]:
        r""" We return back the slope + y intercept

        This work is overkill since we actually don't care about any detail of the line
        just that there are X points on a line!

        Reference:
        https://faculty.cs.niu.edu/~hutchins/csci297p2/webpages/best-fit.htm
        """

        # Check edge cases if horizontal or vertical
        allX = list(map(itemgetter(0), points))
        allY = list(map(itemgetter(1), points))

        if len(set(allY)) == 1:
            initY = allY[0][1]
            return (0, initY)
        elif len(set(allX)) == 1:
            slope = float('inf')
            return (slope, 0)

        length = len(points)
        sumX = sum(allX)
        sumY = sum(allY)
        sumX2 = sum(number * number for number in allX)
        sumXY = sum(x * y for x,y in points)

        meanX = sumX / length
        meanY = sumY / length

        slope = (sumXY - sumX * meanY) / (sumX2 - sumX * meanX)
        initY = meanY - slope * meanX
        return (slope, initY)

    def checkPoints(self, points: List[List[int]]) -> int:
        slope, initY = self.calculateBestFitLine(points)

        matched = 0
        for x, y in points:
            if y == (slope * x) + initY:
                matched += 1

        return matched

    def getSlope(self, leftPoint: List[int], rightPoint: List[int]) -> int:

        x1, y1 = leftPoint
        x2, y2 = rightPoint
        deltaX, deltaY = x2 - x1, y2 - y1

        return float('inf') if deltaX == 0 else deltaY / deltaX

    def maxPoints(self, points: List[List[int]]) -> int:
        r"""
        We need to group closest points together.
        Let's use slope between two points and find the ones that match the most

        There can be anyway from 1 to n points on the same line.
        """

        # 2 points always makes a line, 1 point is the min
        pointCount = len(points)
        if pointCount <= 2:
            return pointCount

        maxNumberOfPoints = 1
        # Given 1 point p, there are n-1 points that can pair with it (not counting itself)
        PAIR_COUNT = pointCount - 1

        currentPairCount = 0
        slopeCount = defaultdict(int)

        # Permutations orders works well in our case since given o
        for leftPair, rightPair in permutations(points, 2):
            currentPairCount += 1

            slope = self.getSlope(leftPair, rightPair)
            slopeCount[slope] += 1

            if currentPairCount == PAIR_COUNT:

                # This gives us number of matching slopes.
                # We want points so include the initial point.
                currentMaxAmountOfPoints = max(slopeCount.values()) + 1
                maxNumberOfPoints = max(maxNumberOfPoints, currentMaxAmountOfPoints)

                # Reset value
                currentPairCount = 0
                slopeCount.clear()

        return maxNumberOfPoints


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))

