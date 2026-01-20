from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        r"""Original solution. This requires getting the shortest possible length
        BEFORE checking so we don't fall out of bounds.
        """

        # Empty Input
        if not strs:
            return ""

        # If we only have 1 input, that is the longest one fir itself
        strListCount = len(strs)
        if strListCount == 1:
            return strs[0]

        # Get max possible length of the prefix
        maxPrefixLength = min(len(x) for x in strs)
        if maxPrefixLength == 0:
            return ""

        # Runs through the shortest length we can get and check if it's the same
        longestPrefix = []
        for index in range(maxPrefixLength):

            currentPrefix = None
            for eachStr in strs:
                if currentPrefix is None:
                    currentPrefix = eachStr[index]
                elif currentPrefix != eachStr[index]:
                    return "".join(longestPrefix)

            longestPrefix.append(currentPrefix)

        return "".join(longestPrefix)


    def longestCommonPrefix2(self, strs: List[str]) -> str:
        r""" Alternative solution where we check until we hit the end or IndexError
    	"""

        # Empty Input
        if not strs:
            return ""

        # If we only have 1 input, that is the longest one fir itself
        strListCount = len(strs)
        if strListCount == 1:
            return strs[0]

        longestPrefix = []
        for index in range(len(strs[0])):

            currentPrefix = strs[0][index]

            for eachStr in strs[1:]:
                try:
                    if currentPrefix != eachStr[index]:
                        return "".join(longestPrefix)
                except IndexError:
                    return "".join(longestPrefix)

            longestPrefix.append(currentPrefix)

        return "".join(longestPrefix)

