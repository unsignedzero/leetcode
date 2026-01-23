class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        if not nums:
            return []

        intervals = []
        currentValue = lastElement = nums[0]

        for currentElement in nums[1:]:
            if currentValue + 1 == currentElement:
                currentValue += 1
            else:
                 if lastElement == currentValue:
                     intervals.append(f"{lastElement}")
                 else:
                     intervals.append(f"{lastElement}->{currentValue}")
                 lastElement = currentValue = currentElement

        if lastElement == currentValue:
             intervals.append(f"{lastElement}")
        else:
             intervals.append(f"{lastElement}->{currentValue}")

        return intervals

