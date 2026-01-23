from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        r""" Shameless copied from https://leetcode.com/problems/insert-interval/solutions/844549/python-super-short-simple-clean-solution-d03a/ and simplified
        """

        result = []
        currentLeft, currentRight = newInterval

        for left, right in intervals:
            # The current value is before the new interval
            if right < currentLeft:
                result.append((left, right))

            # The new interval before the current interval. "Swap" element
            elif left > currentRight:
                result.append((currentLeft, currentRight))
                currentLeft, currentRight = left, right

            # Intervals overlap so we combine them
            elif right >= currentLeft or left <= currentRight:
                currentLeft = min(left, currentLeft)
                currentRight = max(right, currentRight)

        # Store the last element
        result.append((currentLeft, currentRight))
        return result

    def addElement(self, leftIndex: int, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        newLeft, newRight = newInterval
        if leftIndex >= 0:
            found = True
            for rightIndex, (left, right) in enumerate(intervals[leftIndex:], leftIndex):

                if intervals[leftIndex][1] < newLeft and newRight < left:
                    return intervals[:leftIndex] + [newInterval] + intervals + rightIndex[1:]

                if not newRight > right:
                    if newRight >= intervals[rightIndex + 1][0]:
                        from code import interact; interact(local=dict(globals(), **locals()))
                        return intervals[:leftIndex] + [[left, intervals[rightIndex][1], ]] + intervals[rightIndex + 2:]
                    else:
                        return intervals[:leftIndex] + [[left, newRight], ] + intervals[rightIndex + 1:]
            else:

                pass

    def insert2(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        r""" Initial solution has too many edge cases to consider and not worth using
        Looking for a better solution online.
        """

        newLeft, newRight = newInterval

        # New interval before first element
        firstLeft, firstRight = intervals[0]
        if newRight < firstLeft:
            intervals.insert(0, newInterval)
            return intervals
        elif newRight == firstLeft or newRight <= firstRight:
            intervals[0][0] = min(newLeft, intervals[0][0])
            return intervals
        elif newLeft <= firstLeft <= newRight:
            if newRight > firstRight:
                return self.addElement(-1, intervals, newInterval)
            else:
                intervals[0][0] = newLeft
            return intervals

        for index, (left, right) in enumerate(intervals):
            if left <= newLeft <= right:
                return self.addElement(index, intervals, newInterval)

        # This means the thing doesn't fit in any of the above interval.
        # It is at the end OR in between two intervals
        else:
            lastLeft, lastRight = intervals[-1]

            # At the end
            if lastLeft <= newLeft <= lastRight:
                intervals[-1][1] = max(newRight, lastRight)
            else:
                intervals.append(newInterval)
                intervals.sort()

        return intervals

if __name__ == '__main__':
    solution = Solution()
    #print(solution.insert([[1,3],[6,9]], [2,5]))
    #print(solution.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4, 8]))
    #print(solution.insert([[0, 3], [8, 9]], [5,6]))
    #print(solution.insert([[1, 5]], [2, 6]))
    #print(solution.insert([[1, 4], [6, 9]], [2, 6]))
