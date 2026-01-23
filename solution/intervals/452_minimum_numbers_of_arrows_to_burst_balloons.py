from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        r""" We can focus on only the right value since we don't care about the left values
        """

        points.sort()
        arrowCount = 1
        remainingRangeRight = points[0][1]

        for left, right in points[1:]:
            #print(f"Looking at range ({left}, {right})")

            # Out of bounds
            if left > remainingRangeRight:
                arrowCount += 1
                remainingRangeRight = right

            # Contained in range
            else:
                remainingRangeRight = min(right, remainingRangeRight)

        return arrowCount

    def findMinArrowShots2(self, points: List[List[int]]) -> int:
        r""" We use the same range intervals strategies for 57.
        """

        sortedBalloons = sorted(points)
        arrowCount = 0
        remainingRangeLeft, remainingRangeRight = sortedBalloons[0]

        for left, right in sortedBalloons[1:]:
            #print(f"Looking at range ({left}, {right})")

            # Out of bounds
            if right < remainingRangeLeft or left > remainingRangeRight:
                arrowCount += 1
                remainingRangeLeft, remainingRangeRight = left, right
            # Contained in range
            elif right >= remainingRangeLeft or left <= remainingRangeRight:
                remainingRangeLeft = max(left, remainingRangeLeft)
                remainingRangeRight = min(right, remainingRangeRight)
            else:
                arrowCount += 1
                remainingRangeLeft, remainingRangeRight = left, right

        arrowCount += 1
        return arrowCount

if __name__ == '__main__':
    solution = Solution()
    print(solution.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))
    print(solution.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))

