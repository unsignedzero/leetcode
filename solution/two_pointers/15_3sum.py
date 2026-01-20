from typing import List, Set
from itertools import combinations

class Solution:
    def checkTwoOnePair(self, numbers: List[int], filterSet: Set[int]) -> Set[int]:
        r""" This checks for the - - + and + + - cases as they are symmetrical
        logic, just different input values.
        """

        result = set()

        for i, j in combinations(numbers, 2):
            target = -1 * (i+j)
            if target in filterSet:
                result.add(tuple(sorted((i, j, target))))

        return result

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        r""" The faster way to calculate this is to manually iterate through
        all possible values that can occur when three numbers become zero.

        This means:
        0 0 0 : Three zeroes
        - 0 + : One zero but a negative, positive pair.
        - - + : Two negatives, one positive
        - + + : One negative, two positives

        are all possible triples in which the sum is zero.
        """

        # We use a set to store as it is possible there are multiple ways
        # generate the same solution and we only want unique ones.
        result = set()

        # Sort out the numbers by their sign
        negativeList, positiveList, zeroList = [], [], []
        for number in nums:
            if number > 0:
                positiveList.append(number)
            elif number < 0:
                negativeList.append(number)
            else:
                zeroList.append(number)

        # Triple zero solution
        if len(zeroList) >= 3:
            result.add((0, 0, 0))

        # Create sets for faster lookup
        negativeSet, positiveSet = set(negativeList), set(positiveList)

        # Focus on the sign pairs
        if zeroList:
            for number in positiveList:
                if -1 * number in negativeSet:
                    result.add((-1 * number, 0, number))

        negativePairSet = self.checkTwoOnePair(negativeList, positiveSet)
        positivePairSet = self.checkTwoOnePair(positiveList, negativeSet)

        # Combine results
        result.update(negativePairSet)
        result.update(positivePairSet)

        return list(result)

    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        r""" Bruteforce solution where we try to get the values to match
        """

        resultSet = set()
        for triple in combinations(nums, 3):
            if sum(triple) == 0:
                resultSet.add(tuple(sorted(triple)))

if __name__ == '__main__':
    solution = Solution()
