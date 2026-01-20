from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        r""" As we only care about the largest delta, we just track when we get
        new lows to calculate profit and at the end
        """

        # Catches an edge case if there is no change in the input
        lowest, highest = min(prices), max(prices)
        if lowest == highest:
            return 0

        bestProfit = 0
        low, high = float('inf'), float('-inf')

        for currentValue in prices:
            # New Low
            if low > currentValue:
                bestProfit = max(max(high - low, 0), bestProfit)
                low = currentValue
                high = float('-inf')

            # New High
            elif currentValue > high:
                high = currentValue

        return max(bestProfit, high - low)

