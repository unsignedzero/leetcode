from typing import List
from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        r""" Use stdlib
        """
        return list(permutations(nums, len(nums)))

    def permute2(self, nums: List[int]) -> List[List[int]]:
        r""" Use recursion to solve it
        """

        result = []

        def dive(k: int, currentValue: List[int], remainingList: List[int]):
            #print(f"k {k}, currentValue {currentValue} remainingList {remainingList}")
            if k == 0:
                # We need to write new copies as we manipulate the current list
                # and don't want to store a reference
                result.append(currentValue.copy())
            else:

                for element in remainingList:
                    currentValue.append(element)

                    # We need to use an actual copy here else we would
                    # modify the original and break logic downstream
                    newRemainingList = remainingList.copy()
                    newRemainingList.remove(element)
                    dive(k-1, currentValue, newRemainingList)
                    currentValue.pop()

        dive(len(nums), [], nums)
        return result

#if __name__ == '__main__':
