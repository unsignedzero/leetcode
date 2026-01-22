from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        r""" Cleaner solution using the index to force unique solution
        if the input is ordered.
        """

        countList = []

        # Remove dups
        newCandidates = sorted(list(set(candidates)))

        def dive(topIndex: int, currentList: List[int], remainingValue: int):

            print(f"index: {topIndex}: currentList: {currentList} remaining: {remainingValue}")
            for index, eachValue in enumerate(newCandidates[topIndex:]):
                if remainingValue - eachValue > 0:
                    currentList.append(eachValue)
                    dive(index + topIndex, currentList, remainingValue - eachValue)
                    currentList.pop()
                elif remainingValue == eachValue :
                    currentList.append(eachValue)

                    countList.append(currentList.copy())
                    currentList.pop()
                else:
                    break

        dive(0, [], target)
        return countList

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        r""" Slow "brute-force" solution but workable
        """

        countList = []
        seen = set()

        # Remove dups
        newCandidates = list(set(candidates))

        def dive(currentList: List[int], remainingValue: int):

            for eachValue in newCandidates:
                if remainingValue - eachValue > 0:
                    currentList.append(eachValue)
                    dive(currentList, remainingValue - eachValue)
                    currentList.pop()
                elif remainingValue == eachValue :
                    currentList.append(eachValue)

                    frequency = str(sorted(currentList))
                    if frequency not in seen:
                        seen.add(frequency)
                        countList.append(currentList.copy())
                    currentList.pop()
                else:
                    break

        dive([], target)
        return countList

if __name__ == '__main__':
    solution = Solution()
    #print(solution.combinationSum([2,3,6,7], 7))
    print(solution.combinationSum([2,3,5], 8))
    #print(solution.combinationSum([2,3], 6))
    #print(solution.combinationSum([3,5,8], 11))
