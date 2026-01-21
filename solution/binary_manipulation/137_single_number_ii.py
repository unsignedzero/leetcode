from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        r""" Numbers can appear three times or once. We want the one that appears
        once. We can use the xor trick but this time track is a number appears once
        or three times which would fall off using two sets of xors and extra logic to
        refeed itself back.

        The dict solution is simpler and ineffiecnt but works for every data type.
        This only works on ints
        """

        singleSeen, pairSeen = 0, 0

        for currentNumber in nums:
            # Update singleSeen and pairSeen
            singleSeen = (singleSeen ^ currentNumber) & ~pairSeen
            pairSeen = (pairSeen ^ currentNumber) & ~singleSeen

        return singleSeen  # The single number remains in "singleSeen"

