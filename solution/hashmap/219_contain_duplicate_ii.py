from collections import defaultdict
from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = defaultdict(list)

        for index, numbers in enumerate(nums):
            position = seen[numbers]
            if len(position):
                if abs(position[-1] - index) <= k:
                    return True
            position.append(index)

        return False

