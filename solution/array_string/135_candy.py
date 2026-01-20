from typing import List

class safeList(list):
    def get(self, index, default=None):
        r""" Removes negative values since we don't want those when checking the list.
        """
        if index >= 0:
            try:
                return self[index]
            except IndexError:
                return default
        else:
            return default

class Solution:
    def candy(self, ratings: List[int]) -> List[int]:
        r""" Since we will do two passes, we will simplify and only check
        one side at a time which seems to solve it.
        """

        ratingsLength = len(ratings)
        candyCount = [1] * ratingsLength

        for index in range(1, ratingsLength):
            if ratings[index] > ratings[index-1]:
                candyCount[index] = candyCount[index-1] + 1

        for index in range(ratingsLength-2, -1, -1):
            if ratings[index] > ratings[index+1]:
                candyCount[index] = max(candyCount[index], candyCount[index+1] + 1)

        return sum(candyCount)

    def candy2(self, ratings: List[int]) -> int:
        r""" This was my original solution I had that was overly complicated.
        It works on some cases but can be simplified which is the new candy solution, above.

        One pass get's about 60% of all cases and doing two passes drop it down to 40% success.
        """
        leftCandyCount = self.calculateCandyCount(ratings)
        rightCandyCount = self.calculateCandyCount(ratings[::-1])[::-1]
        print(leftCandyCount)
        print(rightCandyCount)

        finalCandyCount = map(min, leftCandyCount, rightCandyCount)
        return sum(finalCandyCount)

    def calculateCandyCount(self, ratings: List[int]) -> List[int]:
        r""" If we have to double pass for symmetrical solutions, we should
        probably aim for something simpler as we are making more mistakes then
        a single pass.
        """

        ratings = safeList(ratings)
        ratingsLength = len(ratings)
        candyCount = safeList([1] * ratingsLength)

        for index in range(ratingsLength):
            minRating = min(ratings.get(index - 1, float('inf')), ratings.get(index + 1, float('inf')))
            selfRating = ratings[index]
            print(f">>{index}: minRating {minRating}, selfRating {selfRating}")

            if selfRating > minRating:
                # Get max candy
                maxCandy = max(candyCount.get(index - 1, 0), candyCount.get(index + 1, 0))
                print(f"Setting {maxCandy + 1} ax maxCandy for {index}")
                candyCount[index] = maxCandy + 1

        return candyCount

if __name__ == '__main__':
    solution = Solution()
    #print(solution.candy([1,0,2]))
    #print(solution.candy([1,2,2]))
    #print(solution.candy([29,51,87,87,72,12]))
    print(solution.candy([1,2,87,87,87,2,1]))

