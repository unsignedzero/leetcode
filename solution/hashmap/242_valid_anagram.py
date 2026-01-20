from collections import Counter, defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        r""" This is the faster solution to check if words are anagrams by
        checking their word frequency.
        """

        sCount = Counter(s)
        tCount = Counter(t)
        return sCount == tCount

    def isAnagram2(self, s: str, t: str) -> bool:
        r""" This is the slower solution iterating and counting letters manually.
        """

        sCount = self.getFequency(s)
        tCount = self.getFequency(t)
        return sCount == tCount

    def getFequency(self, s: str) -> dict[str, int]:
        result = defaultdict(int)
        for char in s:
            result[char] += 1
        return result

