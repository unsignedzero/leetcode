class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        r""" Similar to #205 but char <-> word mapping versus char <-> char mapping.
        """
        patternToString, stringToPattern = {}, {}

        sList = s.split()
        if len(sList) != len(pattern):
            return False

        for left, right in zip(pattern, sList):

            if left not in patternToString:
                patternToString[left] = right
            if right not in stringToPattern:
                stringToPattern[right] = left

            if patternToString[left] != right or stringToPattern[right] != left:
                return False

        return True

if __name__ == '__main__':
    print(wordPattern(None, "abba", "dog cat cat fish"))
    print(wordPattern(None, "aaaa", "dog cat cat dog"))

