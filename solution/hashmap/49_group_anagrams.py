from collections import Counter, defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        r""" This is the faster solution since we can sort strings and
        compare the values directly.
        """

        result = defaultdict(list)

        for each_string in strs:
            sorted_string = str(sorted(each_string))
            result[sorted_string].append(each_string)

        return list(result.values())

    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        r""" This is a slower solution using Counter to get precise values to
        compare. We don't need it and using strings work just fine.
        """

        result = defaultdict(list)

        for each_string in strs:
            sorted_string = str(sorted(Counter(each_string).items()))
            result[sorted_string].append(each_string)

        return list(result.values())

