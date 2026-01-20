from operator import sub
from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        r""" We start the beginning and test all possible values together
        by keeping a running count. If we go negative, all past states are
        not valid and we continue calculations
        """

        length = len(gas)
        totalTank = currentTank = 0
        startPosition = 0

        for index in range(length):
            delta = gas[index] - cost[index]
            totalTank += delta
            currentTank += delta

            # The old position is not valid so we 'reset' in the next area index + 1
            if currentTank < 0:
                currentTank = 0
                startPosition = index + 1

        # Did we make it?
        if totalTank >= 0:
            return startPosition

        return -1

    def canCompleteCircuit2(self, gas: List[int], cost: List[int]) -> int:
        r"""We brute force calculate each step along the way
        """

        # Edge case if it's possible, we skip early
        if sum(gas) < sum(cost):
            return -1

        listLength = len(gas)
        # We only care about the delta between gas/cost, not the individual values
        travelDelta = list(map(sub, gas, cost))

        for index, value in enumerate(travelDelta):
            if value < 0:
                continue

            currentSum = value
            for delta in range(1, listLength):
                # Add up our journey and reject if not possible
                currentSum += travelDelta[(index + delta) % listLength]
                if currentSum < 0:
                    break
            else:
                return index

