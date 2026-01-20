from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        r""" Same as maxProfit2 except 1 line"""

        return sum(max(right - left, 0) for left, right in zip(prices, prices[1:]))

    def maxProfit2(self, prices: List[int]) -> int:
        r""" This is a simpler solution where we just add pair values as needed
        since we can sell daily if there is profit.
        """

        bestSum = 0
        for left, right in zip(prices, prices[1:]):
            bestSum += max(right - left, 0)
        return bestSum

    def maxProfit3(self, prices: List[int]) -> int:
        r""" This is my original solution, using what we know from calculus
        to find all the maximas/minimas and calculating from that value.

        We store these into extremes with:
           0 - Normal
           1 - Maxima
          -1 - Minima

        We have to scan per three-element window which implies the first
        and last element are not extremes.

        Sadly does not work.
        """

        length = len(prices)

        if len(prices) == 2:
            return max(prices[1] - prices[0], 0)

        bestSum = 0
        low, high = float('inf'), float('-inf')

        # Since we
        extreme = [0]
        hasChange = False

        # We look at 3 elements at a time. The center one should be the max/min
        for index in range(length - 2):
            left, center, right = prices[index] , prices[index + 1] ,prices[index + 2]

            # Minima
            if (left - center) > 0 and (right - center) > 0:
                hasChange = True
                extreme.append(-1)
            # Maxima
            elif (left - center) < 0 and (right - center) < 0:
                hasChange = True
                extreme.append(1)
            # Neither
            else:
                extreme.append(0)

        #print(f"extreme {extreme}")
        if hasChange:
            # Adds the last element so extreme lines up with price size
            lastValue = prices[0]

            for index, secondDiff in enumerate(extreme):
                if secondDiff == -1:
                    minValue = prices[index]
                elif secondDiff == 1:
                    maxValue = prices[index]
                    #print(f"Seeing values {maxValue} - {minValue}")
                    bestSum += max(maxValue - minValue, 0)

            # Calculate last element change
            bestSum += max(prices[-1] - prices[-2], 0)

        # If we don't see any extremes, the data is linear (increasing, decreasing or flat)
        else:
            return max(prices[-1] - prices[0], 0)

        return bestSum

if __name__ == '__main__':
    a = Solution()
    print(a.maxProfit2([7,1,5,3,6,4]))
