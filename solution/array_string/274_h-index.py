from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        r"""We can calculate the h-index by sorting the citation count,
        reverse it and compare against how many we have seen already.

        Once it goes below, we have the number.
        """

        for index, eachValue in enumerate(reversed(sorted(citations))):
            #print(f"({index}, {eachValue})")

            if eachValue <= index:
                return index

        # In the case where all citations are over the len count, we return that.
        else:
            return len(citations)

