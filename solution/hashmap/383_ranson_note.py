from collections import Counter, defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r""" We can lean on Counter and solve it in 1 line if we wanted.
        """

        ransomCounter = Counter(ransomNote)
        magazineCounter = Counter(magazine)
        return ransomCounter <= magazineCounter

    def canConstruct2(self, ransomNote: str, magazine: str) -> bool:
        r""" This is the original solution where we use the defaultdict to
        store the numbers and compare them. There is a faster solution using
        just Counter.
        """

        leftDict = self.processString(ransomNote)
        rightDict = self.processString(magazine)
        return self.checkDicts(leftDict, rightDict)

    def processString(self, inputString: str) -> dict:
        letterCount = defaultdict(int)
        for eachLetter in inputString:
            letterCount[eachLetter] += 1

        return letterCount

    def checkDicts(self, leftDict: dict, rightDict: dict) -> bool:
        for eachLetter, eachCount in leftDict.items():
            if rightDict[eachLetter] < eachCount:
                return False

        return True

if  __name__ == "__main__":
    solution = Solution()
    print(solution.canConstruct("aab", "baa"))

