from operator import itemgetter
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []

        sortedInterval = sorted(intervals, key = itemgetter(0))
        currentLeft, currentRight = sortedInterval[0]
        for left, right in sortedInterval[1:]:
            if left <= currentRight:
                currentRight = max(currentRight, right)
            else:
                result.append((currentLeft, currentRight))
                currentLeft, currentRight = left, right

        result.append((currentLeft, currentRight))
        return result

